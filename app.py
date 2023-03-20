from flask import request
from core.utils import create_app, init_app, json_response
from api.blog import blogs_bp
from api.post import posts_bp
from api.comment import comments_bp

app = create_app()
app.register_blueprint(blogs_bp, url_prefix='/blog')
app.register_blueprint(posts_bp, url_prefix='/post')
app.register_blueprint(comments_bp, url_prefix='/comment')
init_app(app)


if __name__ == '__main__':
    app.run(host='localhost', port=8000)