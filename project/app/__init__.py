import os
import logging
from flask import Flask
from flask.logging import create_logger
from logging.handlers import RotatingFileHandler
from app.config import Config
from app.api import api


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    flask_logger = create_logger(app)
    if not app.debug and not app.testing:
        if not os.path.exists(Config.LOG_FOLDER):
            os.mkdir(Config.LOG_FOLDER)
        file_handler = RotatingFileHandler(Config.LOG_FILE, maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        flask_logger.addHandler(file_handler)
        flask_logger.setLevel(logging.INFO)
        # app.logger.info('Upwbp startup')
        with app.app_context():
            api.init_app(app)
            # from app import routes
    return app