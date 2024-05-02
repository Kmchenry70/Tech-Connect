from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required
from techconnect.db import get_db

bp = Blueprint('interests', __name__, url_prefix='/interests')

@bp.route('/interests', methods=['GET', 'POST'])
def interests():
    return render_template('interests.html')