from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required

from techconnect.db import get_db

bp = Blueprint('profile', __name__)

@bp.route('/profile')
@login_required
def profile():
    template_name = 'app/profile.html'
    user_id = g.user['id']
    username = g.user['username']

    db = get_db()
    interests = db.execute(
        'SELECT Interests.interestName FROM UserInterests '
        'JOIN Interests ON UserInterests.interestID = Interests.interestID '
        'WHERE UserInterests.id = ?',
        (user_id,)
    ).fetchall()

    user_interests = [interest['interestName'] for interest in interests]

    return render_template(template_name, template_name=template_name, username=username, interests=user_interests)