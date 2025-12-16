ML Energy Consumption Prediction
================================

Este proyecto es un ejercicio práctico de análisis de datos y machine learning enfocado en un contexto ingenieril.  
El objetivo es analizar el consumo energético de distintas piezas mecánicas y predecir la energía consumida en función del tiempo de operación utilizando regresión lineal en Python.

Este proyecto fue desarrollado como parte de mi proceso de aprendizaje en Machine Learning y Data Analysis.

PROBLEMA

En sistemas mecánicos e industriales, el consumo de energía suele estar relacionado con el tiempo de operación de los componentes.  
Poder estimar este consumo permite:
- Analizar eficiencia
- Detectar comportamientos anómalos
- Optimizar procesos
- Tomar decisiones basadas en datos


DATASET

El dataset contiene información simulada de distintas piezas mecánicas:

Columnas:
- pieza: nombre del componente
- tiempo_operacion: tiempo de funcionamiento en minutos
- energia_consumida: energía consumida por la pieza
- eficiencia: relación entre energía consumida y tiempo de operación

Archivo:
- data/piezas.csv

ANÁLISIS DE DATOS

Durante el análisis se realizaron las siguientes tareas:
- Carga y exploración del dataset con pandas
- Filtrado de datos según condiciones específicas
- Cálculo de estadísticas descriptivas (media, mínimo, máximo, desviación estándar)
- Análisis de correlación entre variables
- Cálculo de eficiencia energética

Se observó una fuerte correlación positiva entre:
- tiempo_operacion
- energia_consumida

MODELO DE MACHINE LEARNING

Se implementó un modelo de regresión lineal para predecir la energía consumida a partir del tiempo de operación.

Librerías utilizadas:
- numpy
- pandas
- scikit-learn

Resultados del modelo:
- Coeficiente (pendiente): ~0.29
- Intercepto: ~1.02
- R²: ~0.94

El valor de R² indica que el modelo explica aproximadamente el 94% de la variabilidad de los datos, lo cual es un buen resultado para un dataset pequeño.

--------------------------------------------------
ESTRUCTURA DEL PROYECTO
--------------------------------------------------
ml-energy-consumption-prediction/
│
├── data/
│   └── piezas.csv
│
├── src/
│   └── train_model.py
│
├── requirements.txt
├── .gitignore
└── README.md


CÓMO EJECUTAR EL PROYECTO

1. Clonar el repositorio
2. Crear un entorno virtual (opcional)
3. Instalar dependencias:

   pip install -r requirements.txt

4. Ejecutar el script:

   python src/train_model.py

PRÓXIMAS MEJORAS

- Visualización de datos con matplotlib
- Separación de datos de entrenamiento y prueba
- Uso de más variables
- Implementación de otros modelos de regresión
- Documentación más detallada del proceso

--------------------------------------------------
AUTOR
--------------------------------------------------
Samuel Martinez  
Estudiante de Ingeniería Mecatrónica  
Interesado en Machine Learning, Data Analysis e Inteligencia Artificial aplicada a la ingeniería


