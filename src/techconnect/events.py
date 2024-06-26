from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required

from techconnect.db import get_db

bp = Blueprint('events', __name__)

@bp.route('/events')
def events():
    template_name = 'app/events.html'

    return render_template(template_name, template_name=template_name)