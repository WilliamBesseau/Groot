from flask import render_template, request, redirect, url_for, session, abort
from sqlalchemy import or_

from app import app, db
from app.models.ideas import Ideas
from app.models.users import User


@app.route('/ideas')
def get_ideas():
    """
    Pagine et renvoie toutes les ideas
    :return:
    """
    q = Ideas.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Ideas.title.ilike('%' + searched + '%'),
            Ideas.description.ilike('%' + searched + '%')
        ))
    ideas = q.paginate(page, 5, False)
    return render_template(
        'ideas.html',
        current_route='get_ideas',
        title='Liste des idées proposées',
        subtitle='',
        data=ideas,
        searched=searched
    )


@app.route('/ideas/new/')
def get_create_idea():
    """
    Renvoie la vue pour créer une nouvelle Idée
    :return:
    """
    user = User.query.filter_by(id=session['uid']).first()

    return render_template(
        'create_idea.html',
        title='Proposez une nouvelle idée de projet',
        data={'user': user}
        )


@app.route('/ideas/create_idea', methods=['POST'])
def create_idea():
    """
    Crée l'idée dans la database
    :return:
    """
    user = User.query.filter_by(id=session['uid']).first()
    title = request.form.get('title')
    description = request.form.get('description')

    idea = Ideas(
        title=title,
        description=description,
        id_user=user.id,
        interested=1
    )

    db.session.add(idea)
    try:
        db.session.commit()
    except:
        abort(500)

    return redirect(url_for('get_ideas'))


@app.route('/ideas/add_interest_idea/<int:id>')
def add_interest_idea(id):
    """
    Ajoute un like sur une idée
    :return:
    """

    idea = Ideas.query.filter_by(id=id).first()
    idea.interested = idea.interested + 1

    try:
        db.session.commit()
    except:
        abort(500)

    return redirect(url_for('get_ideas'))
