from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

#from ..models import Department, Member


class PostForm(FlaskForm):
    """
    Form for students to post enquiries
    """

    cell_number = StringField('Cell Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    enquiry = StringField('Enquiry', validators=[DataRequired()])
    #manager = QuerySelectField(query_factory=lambda: Employee.query.all(),
    #                              get_label="name" )
    submit = SubmitField('Submit')
