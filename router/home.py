import os
from flask import Flask, Blueprint, request, render_template
from werkzeug.utils import secure_filename

home = Blueprint('home', __name__)
app = Flask(__name__)

@home.route('/')
def hello():
    return render_template('home.html')

@home.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        txt=""
        f = request.files['txt_input']

        filename = secure_filename(f.filename)

        f.save('flaskr/static/io/' + filename)
        file = open('flaskr/static/io/' + filename,"r")
        txt = file.readlines()

        #TODO: implement puzzle and send thru template
    return render_template('result.html', txt=txt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, threaded = True, debug = True)