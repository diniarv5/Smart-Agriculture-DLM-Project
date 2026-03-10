import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

# 2. Judul Utama
st.title("🌾 Smart Farming Dashboard - Smart Village")
st.markdown("### 📊 Project: **Smart Agriculture Dataset**")

# 3. Load data dari folder outputs
try:
    df = pd.read_csv('outputs/cleaned_data.csv')
    
    # --- BAGIAN BARU: KEY METRICS (Agar tidak polos) ---
    # Menampilkan ringkasan data di bagian atas
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rata-rata Kelembaban (MOI)", f"{df['MOI'].mean():.2f}")
    with col2:
        st.metric("Suhu Maksimum", f"{df['temp'].max():.2f}°C")
    with col3:
        st.metric("Total Records", len(df))
    st.write("---")

    # --- BAGIAN ALERT (Sistem Peringatan) ---
    latest_moi = df['MOI'].iloc[-1]
    if latest_moi < 30:
        st.error(f"⚠️ **Peringatan Irigasi:** Kelembaban tanah rendah ({latest_moi}). Segera nyalakan pompa!")
    else:
        st.success(f"✅ **Kondisi Aman:** Kelembaban tanah optimal ({latest_moi}).")

    # --- BAGIAN VISUALISASI (Versi Kamu yang Dimodifikasi) ---
    st.subheader("Monitoring Tren Sensor IoT")
    
    # Menaruh selectbox di dalam kolom agar lebih rapi
    c1, c2 = st.columns([1, 3])
    with c1:
        sensor_choice = st.selectbox("Pilih Sensor untuk Grafik:", ["temp", "humidity", "MOI", "result"])
    
    # Grafik Plotly (Otomatis menyesuaikan tema Terang/Gelap Streamlit)
    fig = px.line(df.head(100), 
                 y=sensor_choice, 
                 title=f"Grafik Tren Real-time: {sensor_choice}",
                 markers=True,
                 template="plotly_dark" if st.get_option("theme.base") == "dark" else "plotly_white")
    
    fig.update_traces(line_color='#2ecc71') # Warna hijau khas pertanian
    st.plotly_chart(fig, use_container_width=True)
    
    st.success("🚀 Data berhasil dimuat dari pipeline DLM!")

except Exception as e:
    st.error("❌ File 'outputs/cleaned_data.csv' belum ditemukan atau terjadi error.")
    st.info("Pastikan kamu sudah menjalankan notebook di Colab dan mengupload file .csv ke folder 'outputs' di GitHub.")
