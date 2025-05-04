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

## 🗂️ Struktur Folder
arab_epub_to_text_web/
├── app.py # Web server utama (Flask)
├── epub_to_text.py # Ekstraksi teks dari file EPUB
├── prompt_runner.py # Integrasi prompt dan panggilan API Gemini
├── requirements.txt # Daftar dependensi Python
├── templates/
│ └── index.html # Antarmuka web (HTML, CSS, JS)
└── uploads/ # Folder sementara untuk menyimpan file EPUB yang diunggah

---

## 🛠️ Cara Menjalankan Proyek

### 1. Clone Repository

```bash
git clone https://github.com/username/arab-epub-to-text-llm.git
cd arab-epub-to-text-llm


