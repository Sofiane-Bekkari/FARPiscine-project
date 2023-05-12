from far_app import db

# ALL MODEL DB class

# CLIENT TABLE


class Client(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    nom = db.Column(db.String(length=30), nullable=False)
    prenom = db.Column(db.String(length=30), nullable=False)
    telephone = db.Column(db.String(length=10), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=68), nullable=False)
    add_member = db.Column(db.String(length=20))
    adresse_rue = db.Column(db.String(length=30))
    code_postal = db.Column(db.String(length=8))
    ville = db.Column(db.String(length=10))
    memo = db.Column(db.String(length=10))
    # THE RELATIONSHIP
    # BACK REF USEFUL TO KNOW CLIENT OWNER
    cartes = db.relationship('Carte', backref='owned_user', lazy=True)


# CARTE TABLE
class Carte(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    solde = db.Column(db.Integer(), nullable=False)
    code_pin = db.Column(db.String(length=4), nullable=False)
    type_carte = db.Column(db.String(), nullable=False)
    date_achat = db.Column(db.Date())
    date_exp = db.Column(db.Date())
    # THE FOREIGNKEY
    owner = db.Column(db.Integer(), db.ForeignKey('client.id'))

    # TO CLEAR VIEW ON CLI
    def __repr__(self):
        return f'Carte {self.solde}'
