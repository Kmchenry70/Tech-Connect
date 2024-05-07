from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required
from techconnect.db import get_db

bp = Blueprint('interests', __name__) # url_prefix='/interests'

@login_required
@bp.route('/interests', methods=('GET', 'POST'))
def interests(): 
    template_name = 'app/interests.html'
    if request.method == 'POST':
        sports = request.form.getlist('sports')
        ministries = request.form.getlist('ministries')
        STEM = request.form.getlist('STEM')
        clubs = request.form.getlist('clubs')

        db = get_db()
        error = None
        # This code will run though and check to see if there has been anything filled for these interest. 
        # If none of the interests have at least one selection, then it will store a message that reminds the user to select at least one.
        if not (sports or ministries or STEM or clubs): 
            error = 'Need to select at least one of the options.'

        if error is None: 
            # Need to store data from sports, ministries, STEM, and clubs into the user's database
            user_id = g.user['id']

            try:
                # Start transaction
                db.execute('BEGIN')

                # Clear existing interests
                db.execute(
                    'DELETE FROM user_interests WHERE user_id = ?',
                    (user_id,)
                )
                
                # Compile all interests into one list
                interests = sports + ministries + STEM + clubs
                
                # Insert new interests
                for interest in interests:
                    db.execute(
                        'INSERT INTO user_interests (user_id, interest) VALUES (?, ?)',
                        (user_id, interest)
                    )
                
                # Commit transaction
                db.commit()
            except Exception as e:
                # Roll back in case of error
                db.rollback()
                raise e

            return redirect(url_for("home.home"))

        flash(error)

    return render_template(template_name, template_name=template_name)
        
