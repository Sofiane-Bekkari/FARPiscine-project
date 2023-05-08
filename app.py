from flask import Flask
app = Flask(__name__)


@app.route('/')
def index_page():
    return f'<h1>Welcome to FARPiscine App</h1>'
