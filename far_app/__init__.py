from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
# THIS CONNECTION LOCAL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farpiscien.db'
app.config['SECRET_KEY'] = '41caeef9044a11a7e38c4834'
db = SQLAlchemy(app)
#THIS FOR HASH PW
bcrypt = Bcrypt(app)
#LOGIN MANAGER
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
#THIS REALLY IMPORTANT TO BE AFTER ALL CODES ABOVE
from far_app import routes