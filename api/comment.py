from flask import Blueprint, request

from core.utils import json_response
from models.general import Comment, db

comments_bp = Blueprint(name='comments_bp', import_name=__name__)


@comments_bp.route('/', methods=['GET', 'POST'])
def comments():

    if request.method == 'POST':
        comment = Comment(
            name=request.json.get('name'),
            email=request.json.get('email'),
            phone=request.json.get('phone'),
            )

        db.session.add(comment)
        db.session.commit()

        return json_response(data=comment, status_code=201)

    comments_list = db.session.query(Comment).all()

    return json_response(data=comments_list)


@comments_bp.route('/<int:comment_id>', methods=['GET', 'PUT', 'DELETE'])
def comment_detail(comment_id):
    comment = db.session.query(Comment).get(comment_id)

    if request.method == 'PUT':
        comment.name = request.json.get('name')
        comment.email = request.json.get('email')
        comment.phone = request.json.get('phone')


        db.session.add(comment)
        db.session.commit()

        return json_response(data=comment)

    elif request.method == 'DELETE':
        db.session.delete(comment)
        db.session.commit()

        return json_response(data={'message': 'deleted'})

    return json_response(data=comment)