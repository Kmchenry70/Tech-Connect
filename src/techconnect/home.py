from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from techconnect.auth import login_required
from techconnect.db import get_db

bp = Blueprint('home', __name__)

@app.route('/')
def home():
    return render_template("home.html")