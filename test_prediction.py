import pandas as pd

from src.predict import FraudPredictor

predictor = FraudPredictor()

df = pd.read_csv("data/raw/creditcard.csv")

fraud_sample = df[df["Class"]==1].drop("Class",axis=1).head(10)

predictions , probabilites = predictor.predict(fraud_sample)

print("Predictions")

print(predictions)
print()
print("Fraud Probability")
print(probabilites)