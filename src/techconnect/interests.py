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
    if request.method == 'POST':
        # submit = 
        return redirect(url_for("home.home"))

    return render_template(template_name, template_name=template_name)
        

