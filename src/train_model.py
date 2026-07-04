import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from preprocessing import load_data, clean_data, preprocess_data




df = load_data("data/raw/creditcard.csv")



df = clean_data(df)



X, y, amount_scaler,time_scaler = preprocess_data(df)



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



model = RandomForestClassifier(
    random_state=42,
    n_estimators=100,
    class_weight="balanced",
    n_jobs=-1
)

model.fit(X_train, y_train)



pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))



joblib.dump(amount_scaler, "models/amount_scaler.pkl")
joblib.dump(time_scaler, "models/time_scaler.pkl")

print("\nModel Saved Successfully!")