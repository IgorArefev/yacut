from flask import flash, redirect, render_template, request
from settings import SHORT_LINK_LENGTH

from . import app
from .forms import YacutForm
from .models import URLMap
from .utils import db_save, get_unique_link, original_url


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = YacutForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_link(SHORT_LINK_LENGTH)
        elif not original_url(custom_id):
            form.custom_id.errors = [f'Имя {custom_id} уже занято!']
            return render_template('yacut.html', form=form)
        url_map = URLMap(
            original=form.original_link.data,
            short=custom_id,
        )
        db_save(url_map)
        flash(f'Новая ссылка: '
              f'<a href="{request.base_url}{custom_id}">'
              f'{request.base_url}{custom_id}</a>')
    return render_template('yacut.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def yacut_redirect(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original)
