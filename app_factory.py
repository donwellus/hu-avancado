from flask import Flask

import settings
from blueprints.core import bp

def create_app(app_settings=None):
    if app_settings is None:
        app_settings = settings

    app = Flask(__name__)
    app.config.from_object(app_settings)
    bp.init_app(app, '/')
    bp.init_app(app, url_prefix='/user')

    return app
