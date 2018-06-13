from os.path import join as path_join

from flask import render_template, send_file, redirect, url_for

from app import app
from app.views import dashboard
from app import errors


@app.route('/')
def index():
    print('OK')
    print('OK')
    print('OK')
    return redirect(url_for('get_dashboard'))


@app.route('/static/<path:path>')
def get_static(path):
    try:
        return send_file(path_join(app.root_path, "static", path))
    except IOError as e:
        pass
    return "Not Found", 404
