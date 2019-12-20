from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User, Module


class AddModuleForm(FlaskForm):
    module_code = StringField('Module Code', validators=[DataRequired()])
    title = StringField('Module Name', validators=[DataRequired()])
    staff = StringField('Module Leader', validators=[DataRequired()])
    exam_date = DateField('Examination Date', validators=[DataRequired()])
    submit = SubmitField('Add')


class EditModuleForm(FlaskForm):
    module_code = StringField('Module Code', validators=[DataRequired()])
    title = StringField('Module Name', validators=[DataRequired()])
    staff = StringField('Module Leader', validators=[DataRequired()])
    exam_date = DateField('Examination Date', validators=[DataRequired()])
    submit = SubmitField('Edit')


class GiveScoreForm(FlaskForm):
    score = StringField('Score', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditUserForm(FlaskForm):
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
    submit = SubmitField('Edit')