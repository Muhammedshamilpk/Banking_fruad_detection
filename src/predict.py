import joblib
import pandas as pd



class FraudPredictor:
    def __init__(self):
        
        self.model = joblib.load("models/random_forest.pkl")
        self.amount_scaler = joblib.load("models/amount_scaler.pkl")
        self.time_scaler = joblib.load("models/time_scaler.pkl")
        
    def preprocess(self,df):
        df = df.copy()
        
        df["Amount"] = self.amount_scaler.transform(df[["Amount"]])
        df["Time"] = self.time_scaler.transform(df[["Time"]])
        
        return df
    
    def predict(self,df):
        
        processed = self.preprocess(df) 
        predictions = self.model.predict(processed)
        probabilities = self.model.predict_proba(processed)
        
        return predictions , probabilities[:,1]