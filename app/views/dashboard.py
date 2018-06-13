from pprint import pprint

from flask import render_template, request, redirect, url_for, session, abort
from flask import render_template, request
from sqlalchemy import or_

from app import app, db
from app.models.dash import Dash

@app.route('/dashboard')
def get_dashboard():
    """
    Pagine et renvoie la liste des projets
    :return:
    """
    last_dash = Dash.query.get(1)
    print(last_dash)
    print('**************************')
    print('**************************')
    print('**************************')
    print('**************************')
    print('**************************')
    return render_template(
        'dashboard.html'
        # data=last_dash,
    )
