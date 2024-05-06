from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required
from techconnect.db import get_db

bp = Blueprint('interests', __name__) # url_prefix='/interests'

@bp.route('/interests', methods=('GET', 'POST'))
def interests(): 
    template_name = 'app/interests.html'
    interests = []
    if request.method == 'POST':
        interests.append(request.form('interest'))
        db = get_db()
        error = None

        if len(interests) == 0: 
            error = 'Need to select at least one of the options.'

        if error is None: 
            return redirect(url_for("home.home"))

        flash(error)

    return render_template(template_name, template_name=template_name)
        

