from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.config[
    'SECRET_KEY'] = 'c2cda2df343842ce5db21091b8f5bd8ca593d4a774a687146fdd51bca6941af24bb28c9ab4fce2eb9f7f651eac6578ea299854d22ec76013c9e9c730a1952e73dfe0cbd20fe9e0f5d084ff8a3d58db7b06aed760b0b55956cdc0e07b52a2b7c45bf562'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']='True'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from Fist_app import routes