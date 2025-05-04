import google.generativeai as genai

# Set API Key Gemini
genai.configure(api_key="AIzaSyCeZX2kkajQbo1fnfS7dNKonOVcl2_OGwg")  # Ganti API_KEY_ANDA dengan API Key Gemini kamu

def generate_response(prompt, input_text):
    model = genai.GenerativeModel('gemini-2.0-flash')  # GANTI ke model valid
    
    # Batasi panjang input teks untuk menghindari melebihi batas token
    # Gemini memiliki batas sekitar 1 juta token, tetapi kita buat lebih kecil untuk aman
    # Perkiraan kasar: 1 token ≈ 4 karakter
    MAX_TEXT_LENGTH = 3500000  # Sekitar 200k token, sudah termasuk prompt
    
    # Potong teks jika terlalu panjang
    if len(input_text) > MAX_TEXT_LENGTH:
        # Ambil bagian awal teks
        truncated_text = input_text[:MAX_TEXT_LENGTH]
        print(f"Teks dipotong dari {len(input_text)} karakter menjadi {len(truncated_text)} karakter")
    else:
        truncated_text = input_text
    
    # Tambahkan instruksi untuk memformat output dengan markdown yang benar
    enhanced_prompt = f"{prompt}\n\nPenting: Format output Anda menggunakan markdown yang benar. Gunakan **teks** untuk bold (bukan *teks*), dan gunakan - atau * diikuti spasi untuk bullet points. Pastikan ada baris kosong sebelum daftar bullet points."
    full_prompt = f"{enhanced_prompt}\n\n{truncated_text}"
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        # Tangani error API dengan mengurangi panjang teks lebih lanjut
        if "token count" in str(e).lower() and "exceeds" in str(e).lower():
            # Jika masih error token limit, coba potong lebih pendek
            shorter_text = truncated_text[:len(truncated_text)//2]
            enhanced_prompt = f"{prompt}\n\nPenting: Format output Anda menggunakan markdown yang benar. Gunakan **teks** untuk bold (bukan *teks*), dan gunakan - atau * diikuti spasi untuk bullet points. Pastikan ada baris kosong sebelum daftar bullet points."
            full_prompt = f"{enhanced_prompt}\n\n{shorter_text}\n[TEKS DIPOTONG KARENA TERLALU PANJANG]"
            try:
                response = model.generate_content(full_prompt)
                return response.text + "\n\n[CATATAN: Teks asli terlalu panjang dan harus dipotong. Hanya setengah awal dari dokumen yang diproses.]"
            except Exception as inner_e:
                return f"Error memproses teks: {str(inner_e)}\nCoba lagi dengan file yang lebih kecil atau prompt yang lebih pendek."
        return f"Error memproses teks: {str(e)}\nCoba lagi dengan file yang lebih kecil atau prompt yang lebih pendek."