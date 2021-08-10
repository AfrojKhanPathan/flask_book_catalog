from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class EditBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    format = StringField('Format',validators=[DataRequired()])
    page_num = StringField('pages',validators=[DataRequired()])
    submit = SubmitField('Update')

class CreateBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    avg_rating = FloatField('Rating',validators=[DataRequired()])
    format = StringField('Format',validators=[DataRequired()])
    img_url = StringField('Image',validators=[DataRequired()])
    num_page = IntegerField('Pages',validators=[DataRequired()])
    pub_id = IntegerField('publish id',validators=[DataRequired()])
    submit = SubmitField('Create')
