import os
import hashlib
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
from werkzeug import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = hashlib.sha512(secure_filename(file.filename).encode('utf-8')).hexdigest()

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return redirect(url_for('loading',filename=filename))

@app.route('/loading')
def loading(filename):
    return render_template('loading.html')

@app.route('/results')
def results():
    return render_template('results.html')



if __name__ == '__main__':
    app.run(
            host="0.0.0.0",
            port=int("5000"),
            debug=True
            )

