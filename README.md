# 📖 README – Aplikasi Konversi Tanggal & Jadwal Solat

## ✨ Deskripsi

Aplikasi ini adalah **web app berbasis Streamlit** untuk menampilkan **jadwal waktu solat harian** berdasarkan data lokasi dan tanggal.  
Aplikasi bekerja dengan cara mengubah input berupa:

- **Tanggal (Gregorian)** → Julian Day (JD)
- **Lokasi (lintang, bujur, zona waktu, ketinggian)**  
  → lalu menghitung jadwal solat sesuai parameter tersebut.

---

## 🚀 Fitur

- Input tanggal Gregorian (hari, bulan, tahun).
- Input lokasi: latitude, longitude, timezone (UTC offset), ketinggian.
- Konversi otomatis tanggal Gregorian → Julian Day.
- Perhitungan jadwal solat lengkap (Subuh, Terbit, Zuhur, Ashar, Maghrib, Isya).
- Tampilan antarmuka sederhana via **Streamlit**.

---

## 📂 Struktur Kode

- `converter_gregorian.py` → Modul konversi Gregorian ↔ JD.
- `JDtoJadwalSolat.py` → Modul perhitungan jadwal solat dari JD.
- `app.py` (kode utama di atas) → Antarmuka Streamlit untuk input/output.

---

## 🔧 Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/AzharFkh/Islamic_Prayer_Schedule
   ```
2. Buat virtual environment (opsional tapi direkomendasikan):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   Minimal package yang dibutuhkan:
   - `streamlit`

---

## ▶️ Cara Menjalankan

1. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run main.py
   ```
2. Buka browser di [http://localhost:8501](http://localhost:8501).
3. Isi form input (latitude, longitude, timezone, ketinggian, tanggal).
4. Klik **Cari**, maka jadwal solat akan tampil di layar.

---

## 📥 Input

- **Latitude (L)**: lintang lokasi (°) → positif untuk LU, negatif untuk LS.
- **Longitude (B)**: bujur lokasi (°).
- **Timezone (Z)**: zona waktu relatif UTC (misal +7 untuk WIB).
- **Ketinggian (H)**: elevasi lokasi (meter).
- **Tanggal**: hari, bulan, tahun (Gregorian).

---

## 📤 Output

Aplikasi menampilkan daftar waktu solat:

- Subuh
- Terbit
- Zuhur
- Ashar
- Maghrib
- Isya

---

## ⚖️ Catatan

- Perhitungan jadwal solat didasarkan pada algoritma astronomi sederhana (konversi JD + rumus hisab waktu solat).
- Hasil mungkin sedikit berbeda dengan aplikasi resmi (misal dari Kementerian Agama) karena perbedaan metode dan parameter.
