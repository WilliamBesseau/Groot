import datetime
from datetime import timedelta
from pprint import pprint

from flask import render_template, request, redirect, url_for, session, abort
from flask import render_template, request
from sqlalchemy import or_

from app import app, db
from app.models import dash
from app.models.dash import Dash

@app.route('/dashboard')
def get_dashboard():
    """
    Pagine et renvoie la liste des projets
    :return:
    """
    dash = Dash.query.get(2)
    d = '1-1-1970 00:00:00' + timedelta(seconds=dash.air.date)

    print(d)
    return render_template(
        'dashboard.html',
        dash=dash
    )
