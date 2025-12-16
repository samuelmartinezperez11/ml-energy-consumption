import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("data/piezas.csv")

X = df[["tiempo_operacion"]]
y = df["energia_consumida"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Coeficiente:", model.coef_[0])
print("Intercepto:", model.intercept_)
print("R2:", r2_score(y, y_pred))
