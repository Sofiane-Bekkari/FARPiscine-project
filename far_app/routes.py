from far_app import app
from flask import render_template, redirect, url_for, flash
from far_app.models import Carte, Client
from far_app.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required
from far_app import db


# HOME/INDEX PAGE
@app.route('/')
def home_page():
    return render_template('index.html')


# CARTES PAGE
@app.route('/carte')
@login_required # REQUIRE CLIENT TO LOGIN BEFORE ACCESS THIS PAGE
def carte_page():

    # This will come from DB Carte Table next
    cartes = Carte.query.all()

    return render_template('carte.html', cartes=cartes)

# RESGISTER CLIENT


@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()
    if form.validate_on_submit():
        # TRY TO CREATE ALL CLIENT DATA
        client_to_create = Client(nom=form.nom.data,
                                  prenom=form.prenom.data,
                                  telephone=form.telephone.data,
                                  email=form.email.data,
                                  password=form.password1.data,
                                  add_member=form.add_member.data,
                                  adresse_rue=form.adresse_rue.data,
                                  ville=form.ville.data,
                                  code_postal=form.code_postal.data,
                                  memo=form.memo.data
                                  )
        db.session.add(client_to_create)
        db.session.commit()
        # LOGIN A NEW ACCOUNT FIRST TIME
        login_user(client_to_create)
        flash(f'Account created successfully! You logged as: {client_to_create.nom}', category='success') 

        # REDIRECT TO CARTE PAGE TO SHOP
        return redirect(url_for('carte_page'))
    
    #CHECK IF THERE ERROR ON VALIDATION
    if form.errors != {}:
        for err_msg in form.errors.values():
            #TRY TO GET THESE ERRORS
            flash(f'There Was an Errors: {err_msg}', category='danger')

    return render_template('register.html', form=form)


# LOGIN PAGE
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        # USE EMAIL TO LOGIN CLIENT
        attempted_email = Client.query.filter_by(email=form.email.data).first()
        #CHECK IF EMAIL & PASSWORD = TRUE
        if attempted_email and attempted_email.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_email)
            flash(f'Success! You are logged in as: {attempted_email.nom}', category='success')
            return redirect(url_for('carte_page'))
        else:
            flash(f'Email or password is not correct! Please try again', category='danger')



    return render_template('login.html', form=form)


#LOGOUT

@app.route('/logout')
def logout_page():

    logout_user()
    flash('You are logout!', category='info')

    return redirect(url_for('home_page'))
