import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.title("ROV Mission Intelligence Platform (RMIP)")
st.subheader("Telemetry Dashboard")

# Upload do arquivo
uploaded_file = st.file_uploader("Upload Mission Log CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Mission Data Preview")
    st.dataframe(df)

    # Gráfico de profundidade
    fig = px.line(df, x='timestamp', y='depth', title='Depth Over Time')
    st.plotly_chart(fig, use_container_width=True)

    # Métricas básicas
    max_depth = df['depth'].max()
    mean_depth = df['depth'].mean()

    col1, col2 = st.columns(2)
    col1.metric("Max Depth (m)", round(max_depth, 2))
    col2.metric("Mean Depth (m)", round(mean_depth, 2))
