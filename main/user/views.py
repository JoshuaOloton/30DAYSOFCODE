from flask import render_template, redirect, url_for, session, flash, request
from main.user import user
from main.user.forms import SignUpForm, LogInForm
from main.models import User, Post
from main import db
from decorators import login_required
from sqlalchemy.exc import IntegrityError

@user.route('/')
@user.route('/home')
def home():
    name = None
    if session.get('id'): 
        # if user is logged in, display username in greeting message
        user = User.query.get(session['id'])
        name = user.username
    return render_template('index.html', name=name)

@user.route('/home/<name>')
def home_greeting(name):
    return render_template('index.html', name=name)

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
    if session.get('id'):
        flash('You are already logged in', 'success')
        return redirect(url_for('user.dashboard'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            # confirm user is already in database and password matches
            session['logged_in'] = True
            session['id'] = user.id
            flash('You are logged in', 'success')
            next = request.args.get('next')
            if next is None:
                next = url_for('user.home')
            return redirect(next)
        flash('user does not exist. Please sign up', 'danger')
        return redirect(url_for('user.signup'))
    return render_template('login.html', form=form)

# logout route
@user.route('/logout', methods=['GET','POST'])
def logout():
    if 'id' not in session:
        flash('You are not logged in', 'danger')
        return redirect(url_for('user.login'))
    session.pop('id', None)
    session['logged_in'] = False
    flash('You are logged out', 'danger')
    return redirect(url_for('user.home'))


@user.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['id'])
    posts = user.posts
    return render_template('dashboard.html',posts=posts)
    