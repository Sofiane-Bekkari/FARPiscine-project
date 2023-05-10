from flask import Flask, render_template
app = Flask(__name__)


# HOME/INDEX PAGE
@app.route('/')
def home_page():
    return render_template('index.html')


# CARTES PAGE
@app.route('/carte')
def carte_page():

    # THIS HARD CODED FOR TEST IMPLEMENTATION WITH KYE VALUE
    cartes = [
        {'id_carte': 1, 'id_client': 1, 'solde': 10, 'code_pin': 0000,
         'type_carte': 60, 'date_achat': '', 'date_expiration': ''
         },
        {'id_carte': 2, 'id_client': 2, 'solde': 45, 'code_pin': 0000,
         'type_carte': 300, 'date_achat': '12.04', 'date_expiration': '30.04'
         },
        {'id_carte': 3, 'id_client': 3, 'solde': 85, 'code_pin': 0000,
         'type_carte': 600, 'date_achat': '12.04', 'date_expiration': '30.04'
         },
        {'id_carte': 4, 'id_client': 4, 'solde': 250, 'code_pin': 0000,
         'type_carte': 'Unlimited', 'date_achat': '12.04', 'date_expiration': '30.04'
         }
    ]

    # This will come from DB Carte Table next
    # cartes = Carte.query.all()

    return render_template('carte.html', cartes=cartes)
