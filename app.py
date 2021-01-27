# coding=utf-8
'''
flask app bootstrap file
'''
import os

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
BASE_DIR = os.path.dirname(__file__)

from flask import Flask, current_app
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask.logging import default_handler
from flask_login import current_user, login_required
from logging import Formatter, FileHandler
from configs.config import configs
from gevent.pywsgi import WSGIServer
from configs.config import DebugConfig
from demo.model import models
from demo.controller import views


def init_app(config=DebugConfig):
    app = create_app(config)
    app.register_blueprint(views.bp)
    return app


def create_app(config, disable_debug_bp=False):
    app = Flask(
        __name__,
        static_folder=None,
        template_folder=None,
    )
    # 配置
    if isinstance(config, str):
        config = configs[config]
    app.config.from_object(config)

    # logging
    create_logger(app)

    # db
    db.init_app(app)
    app.logger.info("init db %s" % config.SQLALCHEMY_DATABASE_URI)

    # views
    import demo.controller.views as main_views

    if not disable_debug_bp:
        app.register_blueprint(main_views.bp)

    return app


def create_logger(app):
    formatter = Formatter('[%(asctime)s] [%(filename)s:%(lineno)d] [%(levelname)s]\t%(message)s')
    default_handler.setFormatter(formatter)

    file_handler = FileHandler(app.config["LOGGING_FILE"])
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(app.config["LOGGING_LEVEL"])


def gevent_run(app, host="127.0.0.1", port=5000):
    print("gevent server staring on http://%s:%s" % (host, port))
    WSGIServer((host, int(port)), app).serve_forever()

