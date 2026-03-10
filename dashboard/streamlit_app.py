import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

# 2. Judul Utama & Deskripsi
st.title("🌾 Smart Farming Dashboard - Smart Village")
st.markdown("""
    ### 📊 Project: **Smart Agriculture Dataset**
    Dashboard ini dirancang untuk memantau kondisi lahan pertanian secara real-time. 
    Melalui pendekatan **Data Lifecycle Management (DLM)**, data sensor diolah untuk memberikan 
    wawasan bagi petani dalam menjaga kesehatan tanaman dan efisiensi sumber daya.
""")

# 3. Load data dari folder outputs
try:
    df = pd.read_csv('outputs/cleaned_data.csv')
    
    # --- BAGIAN METRICS ---
    st.write("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Rata-rata Kelembaban", f"{df['MOI'].mean():.2f}", delta_color="normal")
    with col2:
        st.metric("Suhu Maksimum", f"{df['temp'].max():.2f}°C")
    with col3:
        st.metric("Kelembaban Udara (Avg)", f"{df['humidity'].mean():.1f}%")
    with col4:
        st.metric("Total Data Sensor", len(df))
    st.write("---")

    # --- BAGIAN ALERT (Sistem Peringatan) ---
    latest_moi = df['MOI'].iloc[-1]
    if latest_moi < 30:
        st.error(f"⚠️ **Peringatan Irigasi:** Tingkat kelembaban tanah saat ini rendah ({latest_moi}). Sistem menyarankan aktivasi pompa air.")
    else:
        st.success(f"✅ **Kondisi Tanah Optimal:** Kelembaban tanah mencukupi ({latest_moi}). Tidak diperlukan irigasi tambahan.")

    # --- BAGIAN VISUALISASI ---
    st.markdown("## 📈 Analisis Tren Sensor")
    
    c1, c2 = st.columns([1, 3])
    with c1:
        st.write("### Pengaturan")
        sensor_choice = st.selectbox("Pilih Parameter Sensor:", ["temp", "humidity", "MOI", "result"])
        
        # Penjelasan dinamis berdasarkan pilihan sensor
        descriptions = {
            "temp": "Suhu tanah/lingkungan mempengaruhi laju transpirasi tanaman.",
            "humidity": "Kelembaban udara tinggi dapat memicu munculnya hama/jamur.",
            "MOI": "Indikator utama kecukupan air dalam tanah untuk akar tanaman.",
            "result": "Klasifikasi status akhir berdasarkan penggabungan seluruh sensor."
        }
        st.info(f"**Info Sensor:** {descriptions[sensor_choice]}")
    
    with c2:
        # Warna garis berbeda tiap sensor agar lebih berwarna
        colors = {"temp": "#FF4B4B", "humidity": "#1C83E1", "MOI": "#00C781", "result": "#FFD700"}
        
        fig = px.line(df.head(100), 
                     y=sensor_choice, 
                     title=f"Grafik Tren: {sensor_choice.upper()}",
                     markers=True,
                     template="plotly_dark" if st.get_option("theme.base") == "dark" else "plotly_white")
        
        fig.update_traces(line_color=colors[sensor_choice], line_width=3)
        st.plotly_chart(fig, use_container_width=True)

    # --- BAGIAN KESIMPULAN OTOMATIS ---
    st.markdown("### 📝 Kesimpulan Analisis")
    
    # Logika sederhana untuk kesimpulan berdasarkan sensor yang dipilih
    if sensor_choice == "MOI":
        avg_moi = df['MOI'].head(100).mean()
        st.write(f"Berdasarkan grafik, rata-rata kelembaban tanah berada di angka **{avg_moi:.2f}**. Tren ini menunjukkan bahwa pola pengairan sudah cukup stabil namun perlu diawasi saat menyentuh titik terendah.")
    elif sensor_choice == "temp":
        max_t = df['temp'].head(100).max()
        st.write(f"Suhu tertinggi yang tercatat adalah **{max_t}°C**. Petani disarankan melakukan pemantauan ekstra pada jam-jam dengan suhu ekstrem untuk mencegah tanaman layu.")
    else:
        st.write(f"Data **{sensor_choice}** saat ini menunjukkan fluktuasi normal. Tidak ditemukan anomali data yang signifikan dalam 100 rekaman terakhir.")

    st.divider()
    st.caption("🚀 Data Lifecycle Management Pipeline | Smart Village Project 2026")

except Exception as e:
    st.error(f"❌ Terjadi kesalahan: {e}")
    st.info("Pastikan file 'outputs/cleaned_data.csv' sudah ada di repositori GitHub kamu.")
