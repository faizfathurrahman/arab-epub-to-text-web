# 📚 Arabic EPUB to Text with LLM (Gemini) 🔁🧠

Sebuah aplikasi web sederhana berbasis Flask yang memungkinkan pengguna untuk mengunggah file **EPUB berbahasa Arab**, kemudian mengekstrak teksnya dan memprosesnya menggunakan **LLM (Gemini AI)** berdasarkan prompt yang dimasukkan oleh pengguna. Hasilnya ditampilkan dalam format **markdown yang diformat rapi**.

---

## 🚀 Fitur Utama

- ✅ Upload file `.epub` berbahasa Arab.
- 📖 Ekstraksi teks otomatis dari isi EPUB.
- 💡 Kirim prompt kustom ke model **Gemini** dari Google.
- 🧠 Gunakan **LLM (Gemini 2.0 Flash)** untuk menganalisis atau menerjemahkan teks.
- 📋 Tampilkan hasil LLM dalam format **Markdown** (terformat dengan baik di frontend).
- 📊 Progress bar & notifikasi file besar untuk UX yang lebih baik.
- 🗑️ File dihapus otomatis setelah diproses.

---

## 🛠️ Cara Menjalankan Proyek

### 1. Clone Repository
```bash
git clone https://github.com/username/arab-epub-to-text-llm.git
cd arab-epub-to-text-llm
```

### 2. Install Dependensi
```bash
pip install -r requirements.txt
```

### 3. Tambahkan API Key Gemini
Buka prompt_runner.py dan ubah bagian berikut:
```bash
genai.configure(api_key="YOUR_API_KEY")
```
Ganti YOUR_API_KEY dengan API key Gemini kamu yang aktif. Daftar di: https://aistudio.google.com/app/apikey

### 4. Jalankan Server
```bash
python app.py
```
Buka browser ke http://localhost:5000 dan mulai gunakan aplikasinya

## 🧩 Teknologi yang Digunakan

- Python 3
- Flask – Web framework
- BeautifulSoup + EbookLib – Parsing EPUB dan ekstraksi HTML.
- Google Generative AI (Gemini API) – Pemrosesan bahasa alami.
- JavaScript + Showdown.js – Konversi Markdown ke HTML

## ⚠️ Catatan Penting

- Aplikasi ini tidak menyimpan file atau data pengguna. Semua file dihapus setelah diproses.
- Pastikan ukuran file EPUB tidak terlalu besar (idealnya < 5MB) untuk menghindari error token limit pada API Gemini.
