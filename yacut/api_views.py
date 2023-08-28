from http import HTTPStatus
from re import match
from flask import jsonify, request, url_for

from settings import (
    SHORT_LINK_LENGTH,
    SHORT_LINK_PATTERN,
    SHORT_LINK_MAX_LENGTH
)
from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import db_save, get_unique_link, original_url


@app.route('/api/id/', methods=['POST'])
def index_view_api():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_link(SHORT_LINK_LENGTH)
    elif not original_url(data['custom_id']):
        raise InvalidAPIUsage('Имя "{}" уже занято.'.format(data['custom_id']))
    elif len(data.get('custom_id')) > SHORT_LINK_MAX_LENGTH:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    elif not match(SHORT_LINK_PATTERN, data['custom_id']):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    url_map = URLMap(original=data.get('url'), short=data.get('custom_id'))
    db_save(url_map)

    response = {
        'url': url_map.original,
        'short_link': url_for(
            'yacut_redirect',
            short=url_map.short,
            _external=True,
        ),
    }
    return jsonify(response), HTTPStatus.CREATED


@app.route('/api/id/<string:short>/', methods=['GET'])
def yacut_redirect_api(short):
    redirect = URLMap.query.filter_by(short=short).first()
    if not redirect:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': redirect.original})
