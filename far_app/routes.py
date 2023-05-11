from far_app import app
from flask import render_template
from far_app.models import Carte
from far_app.forms import RegisterForm


# HOME/INDEX PAGE
@app.route('/')
def home_page():
    return render_template('index.html')


# CARTES PAGE
@app.route('/carte')
def carte_page():

    # This will come from DB Carte Table next
    cartes = Carte.query.all()

    return render_template('carte.html', cartes=cartes)

# RESGISTER CLIENT


@app.route('/register')
def register_page():

    form = RegisterForm()
    return render_template('register.html', form=form)
