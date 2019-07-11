from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class EmailForm(FlaskForm):
    name = StringField('First Name', validators=[Required()],render_kw={"placeholder": "First Name"})
    email = StringField('Email', validators=[Required()],render_kw={"placeholder": "Email"})
    subscribe = SubmitField('Subscribe')