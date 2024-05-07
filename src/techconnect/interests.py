from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required
from techconnect.db import get_db

bp = Blueprint('interests', __name__) # url_prefix='/interests'

@bp.route('/interests', methods=('GET', 'POST'))
@login_required
def interests(): 
    template_name = 'app/interests.html'
    username = g.user['username']
    if request.method == 'POST':
        sports = request.form.getlist('sports')
        ministries = request.form.getlist('ministries')
        stem = request.form.getlist('stem')
        recreation = request.form.getlist('recreation')

        db = get_db()
        error = None

        # Compile all interests into one list
        interests = sports + ministries + stem + recreation
        
        # This code will run though and check to see if there has been anything filled for these interest. 
        # If none of the interests have at least one selection, then it will store a message that reminds the user to select at least one.
        if len(interests) == 0: 
            error = 'Need to select at least one of the options.'

        else: 
            # Need to store data from sports, ministries, STEM, and clubs into the user's database
            user_id = g.user['id']

            try:
                # Start transaction
                db.execute('BEGIN')

                # Clear existing interests
                db.execute(
                    'DELETE FROM UserInterests WHERE id = ?',
                    (user_id,)
                )
                
                # Compile all interests into one list
                interests = sports + ministries + stem + recreation
                
                print(interests)

                # Insert new interests
                for interest in interests:

                    # get interest from Interests table
                    interest_row = db.execute(
                        'SELECT interestID FROM Interests WHERE interestName = ?',
                        (interest,)
                    ).fetchone()
                    
                    # insert
                    if interest_row:
                        interest_id = interest_row['interestID']
                        db.execute(
                            'INSERT INTO UserInterests (id, interestID) VALUES (?, ?)',
                            (user_id, interest_id)
                        )
                
                # Commit transaction
                db.commit()
            except Exception as e:
                # Roll back in case of error
                db.rollback()
                raise e
            
            return redirect(url_for("home.home"))

        flash(error)

    return render_template(template_name, username=username, template_name=template_name)
        
