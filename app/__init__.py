from flask import Flask
from .routes import main
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
    db.init_app(app)
    app.register_blueprint(main)
    return app
