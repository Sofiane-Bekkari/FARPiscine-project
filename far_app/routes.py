from far_app import app
from flask import render_template, redirect, url_for, flash
from far_app.models import Carte, Client
from far_app.forms import RegisterForm
from far_app import db


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


@app.route('/register', methods=['GET', 'POST'])
def register_page():

    form = RegisterForm()
    if form.validate_on_submit():
        # TRY TO CREATE ALL CLIENT DATA
        client_to_create = Client(nom=form.nom.data,
                                  prenom=form.prenom.data,
                                  telephone=form.telephone.data,
                                  email=form.email.data,
                                  password_hash=form.password1.data,
                                  add_member=form.add_member.data,
                                  adresse_rue=form.adresse_rue.data,
                                  ville=form.ville.data,
                                  code_postal=form.code_postal.data,
                                  memo=form.memo.data
                                  )
        db.session.add(client_to_create)
        db.session.commit()
        # REDIRECT TO CARTE PAGE TO SHOP
        return redirect(url_for('carte_page'))
    
    #CHECK IF THERE ERROR ON VALIDATION
    if form.errors != {}:
        for err_msg in form.errors.values():
            #TRY TO GET THESE ERRORS
            flash(f'There Was an Errors: {err_msg}', category='danger')

    return render_template('register.html', form=form)
