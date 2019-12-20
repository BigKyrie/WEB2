from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 30), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 30),
                                             Email()])
    name = StringField('Name', validators=[
        DataRequired(), Length(1, 10),
    ])
    department = SelectField('Department',
                             choices=[('The College of Arts & Science', 'The College of Arts & Science'),
                                      ('The School of Law', 'The School of Law'),
                                      ('School of Civil Engineering', 'School of Civil Engineering'),
                                      ('The School of Information', 'The School of Information'), ],
                             validators=[DataRequired()])
    gender = SelectField('Gender',
                         choices=[('Man', 'Man'), ('Women', 'Women'), ], validators=[DataRequired()])
    student_id = StringField('Student ID', validators=[
        DataRequired(), Length(10, 10, message='The length of Student ID must be 10')
    ])
    phone_number = StringField('Phone Number', validators=[
        DataRequired(), Length(11, 11, message='The length of Phone number must be 11')
    ]
                               )
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password',
                              validators=[DataRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')



