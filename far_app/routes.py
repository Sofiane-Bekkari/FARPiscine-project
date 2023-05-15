from far_app import app
from flask import render_template, redirect, url_for, flash, request
from far_app.models import Carte, Client, Member
from far_app.forms import RegisterForm, LoginForm, PurchaseCartForm, AddMemberForm
from flask_login import login_user, logout_user, login_required, current_user
from far_app import db
from far_app.test_time import countdown
from datetime import datetime, timedelta
from far_app.timedown import int_to_time

# HOME/INDEX PAGE
@app.route('/')
def home_page():
    return render_template('index.html')


# CARTES PAGE
@app.route('/carte', methods=['GET', 'POST'])
@login_required # REQUIRE CLIENT TO LOGIN BEFORE ACCESS THIS PAGE
def carte_page():

    ## ADD MEMBER
    member_form = AddMemberForm()
    if member_form.validate_on_submit():
        add_member = request.form.get('add_member')
      
        print('THIS ADD MEMBER /', add_member)
        member_to_add =  Member(member_nom=member_form.nom.data,
                                  member_prenom=member_form.prenom.data,
                                  member_age=member_form.age.data,
                                  owner_member=current_user.id
        )
        db.session.add(member_to_add)
        db.session.commit()
        flash(f'You been added a member {member_to_add.member_prenom}', category='success')
        return redirect(url_for('carte_page'))


    ## BUY CARD
    purchase_form = PurchaseCartForm()
    if request.method == 'POST':
        purchase_carte = request.form.get('purchase_carte')
        p_carte_object = Carte.query.filter_by(solde=purchase_carte).first()
        if p_carte_object:
            p_carte_object.owner = current_user.id
            ## get current time
            current_time = datetime.now()
            current_time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
            p_carte_object.date_achat = current_time_string
            #EXP
            expiration_date = datetime.now() + timedelta(days=30)
            p_carte_object.date_exp = expiration_date
            # ADD TIMER
            carte_min =  int(p_carte_object.type_carte)
            current_user.timer += carte_min 
            #print(f'THIS CARTE MIN: {carte_min} / AND THIS USER TIME: {current_user.timer}')
            #print(int_to_time(current_user.timer))
            db.session.commit()
            flash(f'Congratulation! You buy type of carte {p_carte_object.solde} and you add {p_carte_object.type_carte} munites to your account.', category='success')
            #THIS NEED TO REDIRECT TO CARD PAGE
            return redirect(url_for('carte_page'))
        


    # This will come from DB Carte Table next
    if request.method == "GET":

        user_id = current_user.id 
        cartes = Carte.query.all()
        members = Member.query.filter_by(owner_member=user_id)

        print(f'THIS MEMBER SHIP WITH THIS CLIENT: {members}')

        return render_template('carte.html', cartes=cartes, members=members, purchase_form=purchase_form, member_form=member_form)

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
                                  code_pin=form.code_pin.data,
                                  adresse_rue=form.adresse_rue.data,
                                  ville=form.ville.data,
                                  code_postal=form.code_postal.data,
                                  memo=form.memo.data
                                  )
        # CHECK CODE PIN IF WITH 8 DIGIT
        cp_str = str(client_to_create.code_pin)
        cp_len = len(cp_str)
        if cp_len > 8 or cp_len < 8:
                  flash(f'CODE PIN is uncorrect! Please you must put 8 number', category='danger')
                  return redirect(url_for('register_page'))
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



### THIS ROUTE JUST FOR TEST
@app.route('/count')
def count_page():

     #TEST TIME COUNTER
    n = 20
    count = countdown(n)

    return render_template('count.html', count=count)