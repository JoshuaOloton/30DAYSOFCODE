from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Email, EqualTo, Length
from main.models import User


class NewPostForm(FlaskForm):
    title = StringField('Title',validators=[InputRequired(), Length(min=5)])
    body = TextAreaField('Content',validators=[InputRequired(), Length(min=20)])
    submit = SubmitField('Create Post')