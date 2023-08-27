from random import choices
from string import ascii_letters as letters
from string import digits

from . import db
from .models import URLMap


def get_unique_link(length):
    """Генерация случайной ссылки."""
    pattern = letters + digits
    random_link = ''.join(choices(pattern, k=length))
    while not (
            any(char.isdigit() for char in random_link) or not
            any(char.isalpha() for char in random_link)
    ):
        random_link = ''.join(choices(pattern, k=length))
    if original_url(random_link):
        return random_link
    else:
        get_unique_link(length)


def original_url(short_link):
    """Проверка на уникальность короткого URL."""
    return URLMap.query.filter_by(short=short_link).first() is None


def db_save(obj):
    """Сохранение в БД"""
    db.session.add(obj)
    db.session.commit()
