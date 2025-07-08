from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize here

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    #  Lazy import to avoid circular imports
    from .routes import main
    app.register_blueprint(main)

    return app
