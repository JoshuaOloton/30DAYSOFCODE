import email
from flask import render_template, redirect, url_for
from main.user import user
from main.user.forms import SignUpForm
from main.models import User
from main import db

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
        db.session.commit()
        return redirect(url_for('user.home'))
    return render_template('signup.html', form=form)