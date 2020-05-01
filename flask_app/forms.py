from flask_wtf import FlaskForm
from wtforms import *
#       from wtforms_components import ColorField
from wtforms.validators import Length, DataRequired, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=4,max=24),DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=60)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min=4,max=60),EqualTo('password')])
    submit = SubmitField('Sign up')
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[Length(min=4,max=24),DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4,max=60)])
    remeber = BooleanField('Remeber Me')
    submit = SubmitField('Login')
