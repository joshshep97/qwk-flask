from flask import render_template, url_for
from . import bp

@bp.route('/')
@bp.route('/home/')
def home():
    return render_template(
        'index.html',
        title='Home',
    )