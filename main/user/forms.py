from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo, Length
from main.models import User

class SignUpForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(), Length(min=5)])
    email = StringField('Email',validators=[InputRequired(), Email()])
    password = PasswordField('Password',validators=[InputRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[InputRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')
    

class LogInForm(FlaskForm):
    email = StringField('Email',validators=[InputRequired(), Email()])
    password = PasswordField('Password',validators=[InputRequired()])
    submit = SubmitField('Log In')
