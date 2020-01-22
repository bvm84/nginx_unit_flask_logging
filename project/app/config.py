import os
import sys
from pathlib import PurePath
class Config:
    SECRET_KEY = 'somekey'
    SEND_FILE_MAX_AGE_DEFAULT = 1
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FOLDER = str(PurePath(os.getcwd(), 'project', 'app', 'log'))
    LOG_FILE = str(PurePath(os.getcwd(), 'project', 'app', 'log', 'flask.log'))