import streamlit as st
import pandas as pd
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
    
from src.predict import FraudPredictor
from dashboard import show_metrics, show_bar_chart, show_prediction_table
from components import download_predictions
from styles import load_css


st.set_page_config(
  page_title = "Banking Fraud Detection",
  page_icon = "🏦",
  layout = "wide"   
)

load_css()

st.markdown("""
<div class="title">
🏦 Banking Fraud Detection Dashboard
</div>

<div class="subtitle">
AI Powered Credit Card Fraud Detection System
</div>
""", unsafe_allow_html=True)

st.markdown("## 📂 Upload Transaction Dataset")

uploaded_file = st.file_uploader(
    "Upload Transaction CSV",
    type=["csv"],
    label_visibility="collapsed"
)

if uploaded_file :
    df = pd.read_csv(uploaded_file)
    
    st.success("✅ Dataset Uploaded Successfully")
    
    st.subheader("Dataset Preview")
    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        predict = st.button(
            "🚀 Predict Fraud",
            use_container_width=True
        )
    
    if predict:
        predictor = FraudPredictor()
        
        if "Class" in df.columns:
            X=df.drop("Class",axis=1)
            
        else:
            X=df.copy()
            
        predictions,probabilities = predictor.predict(X)
        
        df["Prediction"]=predictions
        df["Fraud Probability"]=probabilities
        
        total = len(df)
        fraud = (df["Prediction"]==1).sum()
        genuine = (df["Prediction"]==0).sum()
        
        show_metrics(total,fraud,genuine)
        
        show_bar_chart(fraud,genuine)
        
        
        show_prediction_table(df)
        
        download_predictions(df)
        
        
        