from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required

from techconnect.db import get_db
# from techconnect.db import Clubs, Events

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    template_name = 'app/home.html'
    username = g.user['username']

    # clubs = Clubs.query.all()

    # clubs = ['ACE', 'SWE', "IEEE", 'ACM']

    # events = Events.query.all()

    return render_template(template_name, template_name=template_name, username=username)