"""Validación sin red: sintaxis, muestreo y escrituras inmutables simuladas."""
import ast
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd

notebook = json.loads(Path(__file__).with_name('01_preprocesamiento.ipynb').read_text())
ns = dict(np=np, pd=pd, hashlib=hashlib, SEMILLA=42, ETIQUETAS=[0,2,4,8,12,16], N_PILOTO=10)
funciones = {'sha', 'resolver_columnas', 'preparar_catalogo', 'seleccionar_piloto', 'crear_inmutable'}
cantidad = 0
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] != 'code':
        continue
    tree = ast.parse(''.join(cell['source']))
    cantidad += 1
    assert notebook['cells'][i+1]['cell_type'] == 'markdown'
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in funciones:
            exec(compile(ast.Module(body=[node], type_ignores=[]), '<notebook>', 'exec'), ns)

raw = pd.DataFrame([{'RA': 12 + e + j/1000, 'DEC': -10+j/100, 'label':e}
                    for e in ns['ETIQUETAS'] for j in range(30 if e == 0 else 3)])
cols = ns['resolver_columnas'](raw, {})
tabla, excluidas, duplicadas = ns['preparar_catalogo'](raw, cols)
a = ns['seleccionar_piloto'](tabla)
b = ns['seleccionar_piloto'](tabla.sample(frac=1, random_state=123))
assert a.objeto_id.tolist() == b.objeto_id.tolist()
assert len(a) == 10 and a.objeto_id.nunique() == 10 and set(a.label) == set(ns['ETIQUETAS'])
for counts in ([1,1,1,1,1,5], [20,1,1,1,1,1], [2,2,2,2,1,1]):
    t = pd.DataFrame([{'label':e,'objeto_id':f'{e}-{j}'} for e,n in zip(ns['ETIQUETAS'],counts) for j in range(n)])
    assert len(ns['seleccionar_piloto'](t)) == 10

def debe_fallar(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Se esperaba ValueError')

debe_fallar(lambda: ns['seleccionar_piloto'](tabla[tabla.label.ne(16)]))
debe_fallar(lambda: ns['resolver_columnas'](raw.assign(ra=1), {}))
conflicto = pd.DataFrame({'RA':[1,1], 'DEC':[2,2], 'label':[0,2]})
debe_fallar(lambda: ns['preparar_catalogo'](conflicto, cols))
invalida = pd.DataFrame({'RA':[np.nan,360,10,10], 'DEC':[0,0,91,0], 'label':[0,2,4,99]})
assert len(ns['preparar_catalogo'](invalida, cols)[1]) == 4

class PreconditionFailed(Exception): pass
class Blob:
    generation = 1
    def __init__(self): self.data = None
    def upload_from_string(self, contenido, **kw):
        assert kw['if_generation_match'] == 0
        if self.data is not None: raise PreconditionFailed()
        self.data = contenido
    def reload(self): pass
    def download_as_bytes(self, **kw):
        assert kw['if_generation_match'] == 1
        return self.data
class Bucket:
    def __init__(self): self.objects = {}
    def blob(self, nombre): return self.objects.setdefault(nombre, Blob())
ns.update(bucket=Bucket(), PreconditionFailed=PreconditionFailed)
f = ns['crear_inmutable']
f('test', b'original')
f('test', b'original')
try:
    f('test', b'diferente')
except RuntimeError:
    pass
else:
    raise AssertionError('No detectó conflicto')
assert ns['bucket'].blob('test').data == b'original'
print(f'OK: {cantidad} celdas de código, explicaciones, muestreo, validación y no sobrescritura simulada.')
