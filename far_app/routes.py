from far_app import app
from flask import render_template
from far_app.models import Carte


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
