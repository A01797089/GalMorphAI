# GalMorphAI: piloto de preprocesamiento

1. Abre Google Colab y usa **Archivo → Subir notebook** para cargar `01_preprocesamiento.ipynb`.
2. Usa Python 3 y CPU. Revisa la celda de parámetros: proyecto `brave-server-511721-p7`, bucket `galmorphai-science`, catálogo y columnas. Las coordenadas deben estar en grados ICRS.
3. Ejecuta en orden y autentica una cuenta con permisos de lectura/listado y creación de objetos en el bucket. No pegues claves de servicio.
4. Revisa la selección de diez galaxias y el reparto de códigos 0, 2, 4, 8, 12, 16. Si las columnas no se detectan sin ambigüedad, configura `COLUMNAS` y continúa desde esa etapa.
5. Ejecuta la celda del bucle de procesamiento. Sólo solicita esos diez objetos, en serie, con reintentos acotados. Los originales se conservan en `gs://galmorphai-science/raw/legacy_surveys/pilot/<piloto_id>/`.
6. Revisa la tabla de estados, los diagnósticos y las imágenes. Los eventos y manifiestos quedan en `gs://galmorphai-science/metadata/legacy_surveys/pilot/<piloto_id>/`.

Para reanudar, ejecuta otra vez con el mismo catálogo y parámetros. Se recuperan los FITS existentes desde GCS y se vuelve a comprobar su integridad; nunca se reemplazan. Cambiar parámetros o catálogo crea otro identificador. Los archivos problemáticos se conservan y se señalan para revisión.

`completado` significa descarga/recuperación e inspección terminadas; consulta también `calidad`. Las alertas son heurísticas y no determinan aptitud científica ni semántica de etiquetas. No hay entrenamiento ni procesamiento masivo.

La ejecución autenticada completa debe realizarse en Colab. Consulta `VALIDACION.md` para distinguir las pruebas realizadas de las pendientes.

## Versionamiento

Mantén el nombre `01_preprocesamiento.ipynb`. En Colab, usa **Archivo → Guardar una copia en GitHub**, selecciona `A01797089/GalMorphAI`, la rama de trabajo y la ruta `notebooks/01_preprocesamiento.ipynb`. Describe cada cambio en el mensaje de commit. Consulta el historial de GitHub para comparar o recuperar versiones. Los FITS y manifiestos del piloto permanecen en GCS.
