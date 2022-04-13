from flask import render_template, redirect, url_for, session, flash
from main.user import user
from main.user.forms import SignUpForm, LogInForm
from main.models import User
from main import db
from main.decorators import login_required
from sqlalchemy.exc import IntegrityError

@user.route('/')
@user.route('/home')
def home():
    name = 'Joshua Oloton'
    return render_template('index.html', name=name)

@user.route('/home/<username>')
def home_greeting(username):
    return render_template('index.html', username=username)

@user.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
            )
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('username/email is taken! Try another', 'danger')
            return redirect(url_for('user.signup'))
        flash('Account successfully created. Please login with your details', 'success')
        return redirect(url_for('user.login'))
    return render_template('signup.html', form=form)

@user.route('/login', methods=['GET','POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            # confirm user is already in database and password matches
            session['logged in'] = True
            session['id'] = user.id
            flash('You are logged in', 'success')
            return redirect(url_for('user.home'))
        flash('user does not exist', 'danger')
    return render_template('login.html', form=form)

@user.route('/logout', methods=['GET','POST'])
def logout():
    if 'user' not in session:
        flash('You are not logged in', 'danger')
        return redirect(url_for('user.login'))
    session.pop('id',None)
    session['logged in'] = False
    flash('You are logged out', 'danger')
    return redirect(url_for('user.home'))