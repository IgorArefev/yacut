from flask_wtf import FlaskForm
from settings import SHORT_LINK_PATTERN
from wtforms import SubmitField, URLField
from wtforms.fields import StringField
from wtforms.validators import URL, DataRequired, Length, Regexp


class YacutForm(FlaskForm):
    original_link = URLField(
        'Оригинальный URL',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректный адрес URL'),
        ],
    )
    custom_id = StringField(
        'Короткое название',
        validators=[
            Length(max=16, message='Слишком длинный URL'),
            Regexp(
                SHORT_LINK_PATTERN,
                message='Только буквы и цифры',
            ),
        ],
    )
    submit = SubmitField('Создать короткий URL')
