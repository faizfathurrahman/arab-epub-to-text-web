import os
from flask import Flask, request, render_template, jsonify
from epub_to_text import extract_text_from_epub
from prompt_runner import generate_response

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'epub'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', output=None)

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files or 'prompt' not in request.form:
        return jsonify({"error": "File atau prompt tidak ditemukan."})
    
    file = request.files['file']
    prompt = request.form['prompt']
    
    if file.filename == '':
        return jsonify({"error": "Tidak ada file yang dipilih."})
    
    if file and allowed_file(file.filename):
        try:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # Ekstrak teks dari EPUB
            try:
                extracted_text = extract_text_from_epub(filepath)
                
                # Tambahkan informasi ukuran teks
                text_size_kb = len(extracted_text) / 1024
                print(f"Ukuran teks yang diekstrak: {text_size_kb:.2f} KB")
                
                # Proses teks dengan Gemini API
                output = generate_response(prompt, extracted_text)
                
                # Hapus file setelah diproses
                try:
                    os.remove(filepath)
                except Exception as e:
                    print(f"Warning: Gagal menghapus file temporary: {str(e)}")
                
                return jsonify({
                    "output": output,
                    "textSize": f"{text_size_kb:.2f} KB"
                })
                
            except Exception as e:
                return jsonify({"error": f"Gagal mengekstrak teks dari EPUB: {str(e)}"})
                
        except Exception as e:
            return jsonify({"error": f"Gagal memproses file: {str(e)}"})
    
    return jsonify({"error": "Format file tidak diperbolehkan."})

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)