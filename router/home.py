import logging
import os, sys
from flask import Flask, Blueprint, request, render_template
from werkzeug.utils import secure_filename

home = Blueprint('home', __name__)
app = Flask(__name__)

@home.route('/')
def hello():
    return render_template('home.html')

@home.route('/result', methods=['POST', 'GET'])
def result():
    txt=""
    path=""
    if request.method == 'POST'and 'txt_file' in request.files:
        list_of_files = request.files.getlist('txt_file')
        if len(list_of_files) > 1:
            error = "I can only process one puzzle at a time."
            return render_template('home.html', error=error)
        f = request.files['txt_input']
        f.save(os.path.join('flaskr/static/io/', secure_filename(f.filename)))
        f.seek(0)
        txt = f.read()
        txt = str(txt, 'utf-8')
        #TODO: implement puzzle and send thru template
    return render_template('result.html', p=path, txt=txt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, threaded = True, debug = True)