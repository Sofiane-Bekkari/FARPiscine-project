from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from far_app.models import Client

# REGISTER CLIENT FROM


class RegisterForm(FlaskForm):

    #CHECK IF THERE EXIST UNIQUE FIELD ON VALIDATION
    def validate_telephone(self, telephone_to_check):
        telephone = Client.query.filter_by(telephone=telephone_to_check.data).first()
        if telephone:
            raise ValidationError('Telephone already exists! Please try a different phone number!')
    #CHECK THIS SECOND UNIQUE FIELD ON VALIDATION
    def validate_telephone(self, email_to_check):
        email = Client.query.filter_by(telephone=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists! Please try a different email adresse!')

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
