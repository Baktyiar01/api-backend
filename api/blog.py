from flask import Blueprint, request

from core.utils import json_response
from models.general import Blog, db

blogs_bp = Blueprint(name='blogs_bp', import_name=__name__)


@blogs_bp.route('/', methods=['GET', 'POST'])
def blogs():

    if request.method == 'POST':
        blog = Blog(
            title=request.json.get('title'),
            description=request.json.get('description'),
            admin_name=request.json.get('admin_name'),
        )

        db.session.add(blog)
        db.session.commit()

        return json_response(data=blog, status_code=201)

    blogs_list = db.session.query(Blog).all()

    return json_response(data=blogs_list)


@blogs_bp.route('/<int:blog_id>', methods=['GET', 'PUT', 'DELETE'])
def blog_detail(blog_id):
    blog = db.session.query(Blog).get(blog_id)

    if request.method == 'PUT':
        blog.title = request.json.get('title')
        blog.description = request.json.get('description')
        blog.admin_name = request.json.get('admin_name')

        db.session.add(blog)
        db.session.commit()

        return json_response(data=blog)

    elif request.method == 'DELETE':
        db.session.delete(blog)
        db.session.commit()

        return json_response(data={'message': 'deleted'})

    return json_response(data=blog)