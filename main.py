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

        return redirect(url_for('loading'))

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/results')
def results():
    output = open("uploads/4461d6a1a2119375a271126ecf937ba915574b2ac50dffa85c06222788110be1ade75544a55c01c62bba902b9a96813cd60f8d72f863b45098943de8127d24a4.txt", "r").read()
    bird = output.rpartition('-')[0]
    notbird = output.rpartition('-')[2]
    return render_template('results.html', bird=bird, notbird=notbird)



if __name__ == '__main__':
    app.run(
            host="0.0.0.0",
            port=int("5000"),
            debug=True
            )

