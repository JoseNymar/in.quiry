from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Student


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    admission = StringField('Admission Number', validators=[DataRequired()])
    home_number = StringField('Home Number', validators=[DataRequired()])
    cell_number = StringField('Cell Number', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    #def validate_admission(self, field):
        #if Student.query.filter_by(admission=admission).first():
            #raise ValidationError('Admission Number is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    admission = StringField('Admission Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
