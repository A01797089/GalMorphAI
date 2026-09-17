# GalMorphAI
### Framework reproducible de visión computacional para la detección y clasificación de barras y anillos en galaxias mediante IA agéntica

## Descripción del proyecto

**GalMorphAI** es un proyecto de investigación orientado al desarrollo de un framework reproducible para la detección y clasificación automática de estructuras morfológicas en galaxias, con énfasis en **barras (bars)** y **anillos (rings)**, utilizando técnicas de Visión Computacional, Aprendizaje Profundo e Inteligencia Artificial Agéntica.

El proyecto busca integrar un flujo completo que abarque desde la adquisición de datos astronómicos provenientes de catálogos públicos, su procesamiento y análisis, hasta el entrenamiento, evaluación y explicación de modelos de inteligencia artificial capaces de asistir en la clasificación morfológica de galaxias.

Como innovación, GalMorphAI incorpora una arquitectura basada en agentes inteligentes que coordina las diferentes etapas del proceso científico, facilitando la automatización, reproducibilidad y escalabilidad del análisis de grandes volúmenes de datos, considerando la futura explotación científica de observatorios de nueva generación como el **Vera C. Rubin Observatory (LSST)**.

---

# Objetivo

Desarrollar un framework modular y reproducible que permita:

- Detectar automáticamente barras y anillos en galaxias.
- Integrar modelos de Deep Learning especializados en morfología galáctica.
- Automatizar el procesamiento de imágenes astronómicas mediante agentes inteligentes.
- Facilitar la experimentación y comparación de modelos de IA.
- Generar una base tecnológica extensible para futuras investigaciones en astronomía computacional.

---

# Integrantes

| Nombre | Matrrícula | Rol |
|----------|------|----------|
| Valente Cortés Aceves  | A01796958 | En definición |
|Rogelio Geovanni Licona Hernández  | A01797149 | En definición |
| Francisco Vázquez Martínez | A017970809 | En definición |

---
# Roles sugeridos

- Desarrollo de IA y Machine Learning 
- Procesamiento de datos astronómicos y visión computacional 
- Arquitectura del framework e IA Agéntica
---

# Estructura del repositorio

```
GalMorphAI/
├── README.md              # Documentación principal del proyecto
├── LICENSE                # Licencia del proyecto
├── CITATION.cff           # Información para citar el proyecto
├── CONTRIBUTING.md        # Guía para colaboradores

├── configs/               # Archivos de configuración de experimentos

├── data/                  # Datos (catálogos, imágenes y metadatos)

├── docs/                  # Documentación técnica y científica

├── notebooks/             # Análisis exploratorios y prototipos

├── src/
│   └── galmorphai/        # Código fuente del framework

├── scripts/               # Scripts de automatización

├── apps/                  # Aplicaciones e interfaces

├── models/                # Modelos entrenados y checkpoints

├── outputs/               # Resultados de experimentos

├── tests/                 # Pruebas unitarias e integración

└── .github/               # Configuración de GitHub Actions, templates y workflows
```

---

# Flujo general del proyecto

```
Catálogos Astronómicos
          │
          ▼
 Descarga de imágenes
          │
          ▼
 Preprocesamiento
          │
          ▼
 Extracción de características
          │
          ▼
 Modelos de Deep Learning
          │
          ▼
 Clasificación de barras y anillos
          │
          ▼
 Explicabilidad y evaluación
          │
          ▼
 Resultados científicos
```

---

# Tecnologías utilizadas

- Python
- PyTorch
- TIMM
- Zoobot
- Astropy
- NumPy
- Pandas
- OpenCV
- Scikit-learn
- Jupyter Notebook
- Git & GitHub

---

# Estado del proyecto

🚧 En desarrollo

Este repositorio corresponde a la primera versión del framework **GalMorphAI**, cuyo objetivo es establecer una base modular y reproducible para la detección automática de estructuras morfológicas en galaxias. El diseño está pensado para facilitar la incorporación de nuevos modelos, agentes inteligentes y conjuntos de datos en futuras etapas del proyecto.

---

# Licencia

Este proyecto se distribuye bajo la licencia especificada en el archivo **LICENSE**.

---

# Citas

Si este proyecto contribuye a una publicación de investigación cientifica, por favor considera citarlo utilizando la información incluida en **CITATION.cff**.
