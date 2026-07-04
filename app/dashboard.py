import streamlit as st
import pandas as pd 
import plotly.express as px



def show_metrics(total,fraud,genuine):

    rate = (fraud/total)*100

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "📊 Transactions",
        f"{total:,}"
    )

    col2.metric(
        "🚨 Fraud",
        fraud
    )

    col3.metric(
        "✅ Genuine",
        genuine
    )

    col4.metric(
        "📈 Fraud Rate",
        f"{rate:.3f}%"
    )
    
  
def show_bar_chart(fraud, genuine):

    chart_data = pd.DataFrame({
        "Category": ["Fraud", "Genuine"],
        "Count": [fraud, genuine]
    })

    fig = px.bar(
        chart_data,
        x="Category",
        y="Count",
        color="Category",
        text="Count",
        title="Fraud vs Genuine Transactions"
    )

    fig.update_layout(
        showlegend=False,
        xaxis_title="Transaction Type",
        yaxis_title="Count"
    )

    st.plotly_chart(fig, width="stretch")
 

   
def show_prediction_table(df):
    result_df = pd.DataFrame({
    "Time":df["Time"],
    "Amount":df["Amount"],
    "Prediction":df["Prediction"].map({
        0:"Genuine",
        1:"Fraud"
    }),
    "Fraud Probability (%)":(df["Fraud Probability"] * 100).round(2)
    })
    
    st.subheader("Prediction Results")
    st.dataframe(result_df.head(20))
    st.subheader("🚨 Fraud Transactions")
    
    fraud_df = result_df[result_df["Prediction"]=="Fraud" ]
    
    st.dataframe(fraud_df)