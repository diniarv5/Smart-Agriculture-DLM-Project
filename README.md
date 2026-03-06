# 🌾 Smart Farming Dashboard - Smart Village Project
**Tugas 2: Data Lifecycle Management**
**Nama:Fivediniar Edra Primaulidina**
**NPM : 23082010046**
**Deadline: 11 Maret 2026**

## 📋 Deskripsi Proyek
Proyek ini bertujuan untuk membangun dashboard monitoring pertanian cerdas () menggunakan dataset sensor IoT. Implementasi ini mengikuti 6 tahapan **Data Lifecycle Management (DLM)** untuk mendukung digitalisasi desa (Smart Village).

---

## 🔄 Data Lifecycle Implementation

### 1. Data Acquisition
* **Sumber Data:** Smart Agriculture Dataset dari Kaggle.
* **Metode:** Diambil secara programmatik menggunakan Kaggle API.
* **Parameter:** Suhu, Kelembaban (Humidity), pH Tanah, dan Curah Hujan (Rainfall).

### 2. Data Storage
* **Raw Data:** Disimpan di folder `data/raw/` dalam format `.csv`.
* **Processed Data:** Disimpan di folder `data/processed/` setelah melalui tahap pembersihan.

### 3. Data Processing
* **Cleaning:** Menghapus *missing values* menggunakan Python (Pandas).
* **Filtering:** Memastikan tipe data sensor bersifat numerik (float/int) untuk menghindari error pada analisis.

### 4. Data Analysis
* Melakukan analisis statistik deskriptif untuk mengetahui rata-rata kondisi lahan.
* Mengidentifikasi korelasi antar variabel (misalnya hubungan antara suhu dan kelembaban).

### 5. Data Visualization
* **Static:** Heatmap korelasi yang dihasilkan di Jupyter Notebook.
* **Interactive:** Dashboard real-time menggunakan **Streamlit** yang mencakup tren sensor dan sistem peringatan dini (*threshold alert*).

### 6. Data Governance & Quality
Berdasarkan evaluasi, kualitas data proyek ini adalah sebagai berikut:

| Dimensi Kualitas | Skor (0-1) | Keterangan |
|---|---|---|
| **Accuracy** | 1.0 | Data berasal dari sumber terverifikasi (Kaggle). |
| **Completeness** | 1.0 | Tidak ada baris yang kosong setelah tahap cleaning. |
| **Consistency** | 0.9 | Format satuan sensor seragam di seluruh dataset. |
| **Timeliness** | 0.8 | Data mencerminkan siklus monitoring yang relevan. |

**Kebijakan Tata Kelola:**
* **Ownership:** Data digunakan untuk kepentingan akademik dan simulasi Smart Village.
* **Retention:** Data mentah akan disimpan selama 1 semester untuk keperluan audit tugas.

---

## 📂 Struktur Repositori
```text
├── dashboard/
│   └── streamlit_app.py                           # Kode utama Dashboard Streamlit
├── data/
│   ├── raw/                                       # Dataset asli dari Kaggle
│       └── Smart_Agriculture_Dataset_Data.csv     # Dataset asli dari Kaggle 
├── outputs/                                       # Bukti pengerjaan (Heatmap & Dashboard)
│   ├── cleaned_data.csv                           # Dataset yang sudah clean
│   ├── analysis report.pdf                        # Laporan analisis
│   └── screenshot_dasnoard.png                    # Gambar dashboard dari Streamlit
├── Data_Lifecycle_Smart_Farming.ipynb
└── README.md                                      # Dokumentasi proyek
