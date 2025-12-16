import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv("data/piezas.csv")

X = data[["tiempo_operacion"]]
y = data["energia_consumida"]


model = LinearRegression()
model.fit(X, y)


y_pred = model.predict(X)


plt.figure()
plt.scatter(X, y)
plt.xlabel("Tiempo de operación (min)")
plt.ylabel("Energía consumida")
plt.title("Energy Consumption vs Operation Time")
plt.show()


plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel("Tiempo de operación (min)")
plt.ylabel("Energía consumida")
plt.title("Linear Regression: Energy Prediction")
plt.show()
