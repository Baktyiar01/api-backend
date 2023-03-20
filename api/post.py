from flask import Blueprint, request

from core.utils import json_response
from models.general import Post, db

posts_bp = Blueprint(name='posts_bp', import_name=__name__)


@posts_bp.route('/', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post = Post(
            title=request.json.get('title'),
            description=request.json.get('description'),
            date_posted=request.json.get('date_posted'),
        )

        db.session.add(post)
        db.session.commit()

        return json_response(data=post, status_code=201)

    posts_list = db.session.query(Post).all()

    return json_response(data=posts_list)


@posts_bp.route('/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def post_detail(post_id):
    post = db.session.query(Post).get(post_id)

    if request.method == 'PUT':
        post.title = request.json.get('title')
        post.description = request.json.get('description')
        post.date_posted = request.json.get('date_posted')

        db.session.add(post)
        db.session.commit()

        return json_response(data=post)

    elif request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()

        return json_response(data={'message': 'deleted'})

    return json_response(data=post)