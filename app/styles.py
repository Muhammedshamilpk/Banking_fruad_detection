import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main{
        background-color:#f5f7fa;
    }

    .title{
        font-size:42px;
        font-weight:700;
        color:#0A2540;
        margin-bottom:5px;
    }

    .subtitle{
        font-size:18px;
        color:#6b7280;
        margin-bottom:30px;
    }

    .metric-card{
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0 2px 8px rgba(0,0,0,.1);
        text-align:center;
    }

    .metric-title{
        color:#666;
        font-size:18px;
    }

    .metric-value{
        font-size:38px;
        font-weight:bold;
        color:#0A2540;
    }

    </style>
    """, unsafe_allow_html=True)