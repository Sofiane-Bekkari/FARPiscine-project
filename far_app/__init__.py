from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# THIS CONNECTION LOCAL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farpiscien.db'
db = SQLAlchemy(app)
