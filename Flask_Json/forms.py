from flask_wtf import FlaskForm
from wtforms import *

class FilterForm(FlaskForm):
    ticket  = SelectField("Ticket", 000000)
    process = SelectField("Process", "XH018")
    question = SelectField("Question", "Do XT018 support RISCV ?")
    topic = SelectField("Topic", "RISCV design")
    answer = SelectField("Answer", "It does support but low speed")
    apply_submit = SubmitField("Apply")
    