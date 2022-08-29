from flask import Flask, render_template, Blueprint

home = Blueprint('home', __name__,)

app = Flask(__name__)

@home.route('/')
def hello():
    return '<p>Hello!</p>'

@home.route('/index')
def scream(greeting):
    return render_template('templates/index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, threaded = True, debug = True)