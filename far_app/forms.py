from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

# REGISTER CLIENT FROM


class RegisterForm(FlaskForm):
    nom = StringField(label='Nom')
    prenom = StringField(label='Prenom')
    telephone = StringField(label='Telephone')
    email = StringField(label='Email')
    password1 = PasswordField(label='Password')
    password2 = PasswordField(label='Confirm password')
    add_member = StringField(label='Member')
    adresse_rue = StringField(label='Adresse & Rue')
    ville = StringField(label='Ville')
    code_postal = StringField(label='Code postal')
    memo = StringField(label='Memo')
    submit = SubmitField(label='Create Account')
