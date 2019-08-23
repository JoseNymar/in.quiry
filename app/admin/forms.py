from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

class PostRespondForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    #department = QuerySelectField(query_factory=lambda: Department.query.all(),
    #                              get_label="dname")
    response= StringField('Response', validators=[DataRequired()])
    #salary= IntegerField('Salary', validators=[DataRequired()])
    submit = SubmitField('Submit')
