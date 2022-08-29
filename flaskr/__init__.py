from flask import Flask
from router.home import home
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    app.register_blueprint(home) #, url_prefix='/home')


    db.init_app(app)
    # from models import 

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000, debug=True)