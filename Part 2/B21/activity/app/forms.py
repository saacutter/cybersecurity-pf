from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, PasswordField, SubmitField, FileField, DateField, TextAreaField
from wtforms.validators import DataRequired, Optional, Email, EqualTo, Regexp, Length, ValidationError
from flask_login import current_user
from app import db, models
import sqlalchemy as sa

class LoginForm(FlaskForm):
    username      = StringField('Username or Email Address', validators=[DataRequired()])
    password      = PasswordField('Password', validators=[DataRequired()])
    remember_user = BooleanField('Remember Me')
    submit        = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username         = StringField('Username', validators=[DataRequired(), Regexp(r'^[a-zA-Z0-9]+$', message="Username must contain only letters and numbers.")])
    password         = PasswordField('Password', validators=[DataRequired(), Length(min=8, message="The password must be at least 8 characters long"), Regexp(r'^[a-zA-Z0-9!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~]+$', message="The password must contain only letters, numbers, and !@#$%^&*()_+=-")])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="The passwords do not match")])
    submit           = SubmitField('Sign Up')

    def validate_username(self, field):
        # Check if username already exists
        existing_user = db.session.scalar(sa.select(models.Users).where(sa.func.lower(models.Users.username) == field.data.lower()))
        if existing_user:
            raise ValidationError("A user with this username already exists")