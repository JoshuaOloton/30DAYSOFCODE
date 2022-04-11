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

    # check if username alreafy exists
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username is taken!')

    # check if username alreafy exists
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email is taken!')
