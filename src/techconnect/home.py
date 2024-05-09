from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required

from techconnect.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/')
@login_required
def home():
    template_name = 'app/home.html'
    username = g.user['username']
    user_id = g.user['id']

    db = get_db()

    # get the user's interests
    user_interests_rows = db.execute(
        'SELECT interestName FROM UserInterests '
        'JOIN Interests ON UserInterests.interestID = Interests.interestID '
        'WHERE UserInterests.id = ?',
        (user_id,)
    ).fetchall()

    # Extract interest names from rows
    user_interests = [row['interestName'] for row in user_interests_rows]

    # num_interests = len(user_interests)

    # print(user_interests)
    # print(num_interests)

    # Fetch the club names from the Clubs table
    club_names_rows = db.execute(
        'SELECT clubName FROM Clubs'
    ).fetchall()

    # Extract club names from rows
    club_names = [row['clubName'] for row in club_names_rows]

    # num_clubnames = len(club_names)

    # print(club_names)
    # print(num_clubnames)

    return render_template(template_name, template_name=template_name, username=username, club_names=club_names)