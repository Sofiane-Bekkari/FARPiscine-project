from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# THIS CONNECTION LOCAL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farpiscien.db'
app.config['SECRET_KEY'] = '41caeef9044a11a7e38c4834'
db = SQLAlchemy(app)
