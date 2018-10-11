from flask import Blueprint, Flask

bp = Blueprint('core', __name__)

@bp.route('/')
def hello_world():
    return 'Hello World!'

def init_app(app:Flask, url_prefix='/'):
    app.register_blueprint(bp, url_prefix=url_prefix)