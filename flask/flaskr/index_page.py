from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('index_page', __name__)

@bp.route('/')
def index():
    return render_template('index_page/index_page.html')