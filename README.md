ML Energy Consumption Prediction
================================

This project is a beginner-friendly Machine Learning application focused on analyzing
energy consumption in mechanical components using Python and Linear Regression.
It was developed as part of my learning path in Data Science and Machine Learning.


Problem Description

In industrial and mechanical systems, understanding how operation time affects
energy consumption is important for improving efficiency and reducing costs.

This project analyzes a small dataset of mechanical parts and:
- Explores relationships between operation time and energy usage
- Calculates efficiency metrics
- Trains a Linear Regression model to predict energy consumption
  based on operation time

--------------------------------------------------
Dataset
--------------------------------------------------
The dataset is a CSV file located in the `data/` folder and contains the following columns:

- pieza: Name of the mechanical component
- tiempo_operacion: Operation time (minutes)
- energia_consumida: Energy consumed
- operaciones_fallidas: Number of failed operations
- eficiencia: Calculated as energia_consumida / tiempo_operacion

Example:

pieza,tiempo_operacion,energia_consumida,operaciones_fallidas,eficiencia
manivela,30,10,1,0.33
palanca,60,20,2,0.33
cpu,80,25,3,0.31


Technologies Used

- Python 3
- NumPy
- Pandas
- Scikit-learn
- Git & GitHub


Model

A Linear Regression model is trained to predict energy consumption
based on operation time.

Model output includes:
- Coefficient
- Intercept
- R² score (coefficient of determination)

This allows evaluation of how well operation time explains
energy consumption.

--------------------------------------------------
Results
--------------------------------------------------
- The model achieves a high R² score, indicating a strong linear relationship
  between operation time and energy consumption.
- Components with lower energy per unit of time are identified as more efficient.
- The project demonstrates basic data analysis, feature engineering,
  and model evaluation.


How to Run the Project

1. Clone the repository

2. Install dependencies:

   pip install -r requirements.txt

3. Run the training script:

   python src/train_model.py

 Visualization

The project includes data visualization to compare real energy consumption
against model predictions using Matplotlib.





Author

Samuel Martinez  
Mechanical Engineering Student  
Aspiring Machine Learning & Data Science Developer
