import streamlit as st

def download_predictions(df):

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Prediction Report",
        csv,
        "fraud_predictions.csv",
        "text/csv"
    )