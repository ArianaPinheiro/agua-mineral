import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn

# Carregar dados
df = pd.read_csv("data/water_sales.csv")

X = df[["temperature"]]
y = df["vendas"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Treinar modelo
model = LinearRegression()

with mlflow.start_run():
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)

    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "model")

    print(f"Modelo treinado com MSE: {mse}")
