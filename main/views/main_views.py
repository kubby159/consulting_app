from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/')
def main_page():
    return redirect(url_for('question._list'))

@bp.route('/content')
def main_content():
    return "Here is Content!"
