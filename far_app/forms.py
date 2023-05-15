from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, number_range
from far_app.models import Client


# REGISTER CLIENT FROM
class RegisterForm(FlaskForm):

    #CHECK IF THERE EXIST UNIQUE FIELD ON VALIDATION
    def validate_telephone(self, telephone_to_check):
        telephone = Client.query.filter_by(telephone=telephone_to_check.data).first()
        if telephone:
            raise ValidationError('Telephone already exists! Please try a different phone number!')
    #CHECK THIS SECOND UNIQUE FIELD ON VALIDATION
    def validate_email(self, email_to_check):
        email = Client.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists! Please try a different email adresse!')

    nom = StringField(label='Nom', validators=[Length(min=3, max=30), DataRequired()])
    prenom = StringField(label='Prenom', validators=[Length(min=3, max=30), DataRequired()])
    telephone = StringField(label='Telephone', validators=[Length(min=10), DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm password', validators=[EqualTo('password1') , DataRequired()])
    code_pin =  IntegerField(label='Code PIN:')
    #code_pin =  IntegerField(label='Code PIN:', validators=[number_range(min=8, max=8, message='Please 8 dig') , DataRequired()])
    adresse_rue = StringField(label='Adresse & Rue')
    ville = StringField(label='Ville')
    code_postal = StringField(label='Code postal')
    memo = StringField(label='Memo')
    submit = SubmitField(label='Create Account')


# LOGIN CLIENT FORM
class LoginForm(FlaskForm):
    email = StringField(label='Email:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

    
# PURCHASE CARTE
class PurchaseCartForm(FlaskForm):
    submit = SubmitField(label='Purchase Card')


# ADD A MEMBER
class AddMemberForm(FlaskForm):
    nom = StringField(label='Nom de member:', validators=[DataRequired()])
    prenom = StringField(label='Prenom de member:', validators=[DataRequired()])
    age = IntegerField(label='Age de member optional:',validators=[number_range(min=1) ,DataRequired()])
    submit = SubmitField(label='Add Member')

    
