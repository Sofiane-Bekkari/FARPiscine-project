from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired

# REGISTER CLIENT FROM


class RegisterForm(FlaskForm):
    nom = StringField(label='Nom', validators=[Length(min=3, max=30), DataRequired()])
    prenom = StringField(label='Prenom', validators=[Length(min=3, max=30), DataRequired()])
    telephone = StringField(label='Telephone', validators=[Length(min=10), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password', validators=[EqualTo('password1') , DataRequired()])
    add_member = StringField(label='Member Prenom')
    adresse_rue = StringField(label='Adresse & Rue')
    ville = StringField(label='Ville')
    code_postal = StringField(label='Code postal')
    memo = StringField(label='Memo')
    submit = SubmitField(label='Create Account')
