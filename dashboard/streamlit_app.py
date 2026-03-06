import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")
st.title("🌾 Smart Farming Dashboard - Smart Village")

# Load data dari folder data/processed yang kamu buat di Colab
try:
    df = pd.read_csv('outputs/cleaned_data.csv')
    
    st.subheader("Monitoring Tren Sensor IoT")
    sensor_choice = st.selectbox("Pilih Sensor:", ["temp", "humidity", "MOI", "result"])
    
    fig = px.line(df.head(100), y=sensor_choice, title=f"Tren {sensor_choice}")
    st.plotly_chart(fig)
    
    st.success("Data berhasil dimuat dari pipeline DLM!")
except:
    st.error("File 'outputs/cleaned_data.csv' belum ditemukan. Pastikan sudah upload hasil dari Colab!")
