from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    name = StringField('Whats your name',validators=[DataRequired(), Length(3,15,message='between 3 to 15')])
    email = StringField('Enter your email',validators=[DataRequired(), Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(5),EqualTo('conform',message="password must match")])
    conform = PasswordField('conform',validators=[DataRequired()])
    submit = SubmitField('Register')
