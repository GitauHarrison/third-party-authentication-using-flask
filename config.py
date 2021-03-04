import os
basedir = os.path.join(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME='tastebolder@gmail.com'
    MAIL_PASSWORD=b'\x99\xa4\x9dOO\xa4\x7f\xb5\xeb\xeb\xa1\x15d\xf3\xb3\xbe'
    ADMINS=['norulesanymore@gmail.com']
