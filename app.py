from flask import Flask, render_template, request, url_for
from utils.bg_remover import remove_background
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'static/output'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', output_url=None)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    file = request.files['image']
    filename = datetime.now().strftime('%Y%m%d%H%M%S') + '_' + file.filename
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(input_path)

    output_filename = 'output_' + filename
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

    remove_background(input_path, output_path)

    output_url = url_for('static', filename=f'output/{output_filename}')
    return render_template('index.html', output_url=output_url)

if __name__ == '__main__':
    app.run(debug=True)
