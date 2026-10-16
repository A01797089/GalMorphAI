# Validación de la entrega

Fecha: 15 de octubre de 2026.

## Comprobaciones realizadas localmente

- Lectura del JSON del notebook, estructura de celdas y metadatos de kernel Python 3.
- Análisis sintáctico Python de las 11 celdas de código.
- Confirmación de una explicación Markdown inmediatamente después de cada celda de código.
- Ejecución de funciones reales extraídas del notebook con NumPy y pandas: piloto de diez objetos únicos, presencia de los seis códigos, independencia del orden de filas y asignación de cuotas con estratos muy pequeños o desbalanceados.
- Rechazo de estratos ausentes, columnas ambiguas, coordenadas inválidas y etiquetas contradictorias en coordenadas idénticas.
- Ejecución de la función de escritura contra un almacenamiento simulado: creación exclusiva, reutilización de contenido idéntico y rechazo de contenido distinto sin alterar el original.

Resultado: todas las comprobaciones anteriores pasaron. El archivo `validar_notebook.py` permite repetirlas con Python, NumPy y pandas instalados.

## Comprobaciones pendientes en Colab

- Instalación y compatibilidad efectiva de dependencias en el runtime elegido.
- Autenticación de la cuenta y acceso al proyecto y al catálogo real.
- Esquema real de columnas, distribución de etiquetas y disponibilidad de diez galaxias elegibles.
- Respuestas HTTP del servicio, inspección FITS/WCS real y visualización.
- Escritura, persistencia y reanudación contra GCS real.
- Pruebas FITS sintéticas incluidas en la última celda del notebook.

La instalación de Astropy, Requests, Matplotlib, nbformat y el cliente GCS en un entorno temporal local no pudo completarse por falta de conectividad de red. Por ello no se afirma haber ejecutado las pruebas FITS ni una validación formal con nbformat. No se descargaron imágenes ni se modificó GCS durante la elaboración.

Las celdas se entregan sin salidas ni contadores de ejecución para evitar presentar resultados sintéticos como datos del catálogo. El notebook registra versiones y resultados reales cuando se ejecuta en Colab.

## Actualización: ejecución proporcionada por el usuario

El notebook versionado conserva salidas de Colab: catálogo de 8,527 filas, diez objetos completados, seis códigos representados y pruebas locales del notebook aprobadas. Los diez objetos tienen calidad `revisar`; falta inspeccionar los avisos del manifiesto. Estas salidas son evidencia aportada por el usuario, no una nueva ejecución realizada durante la incorporación a GitHub. Se centralizó el mapeo `ra`, `dec`, `anillos` y se verificó de nuevo la sintaxis. La descripción anterior de celdas vacías corresponde a la entrega inicial.
