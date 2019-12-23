import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'abcde'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'True')
    MAIL_USERNAME = 'bigkyrie@163.com'
    MAIL_PASSWORD = 'weiyuheng123'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Management]'
    FLASKY_MAIL_SENDER = 'Teaching Admin <bigkyrie@163.com>'
    FLASKY_ADMIN = '978633302@qq.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}







'''import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
MAIL_PORT = int(os.environ.get('MAIL_PORT', '465'))
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true')
MAIL_USERNAME = '18832109159@163.com'
MAIL_PASSWORD = 'wzh690112'
FLASKY_MAIL_SUBJECT_PREFIX = '[STONE]'
FLASKY_MAIL_SENDER = 'STONE Admin <18832109159@163.com>'

  'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
'''



'''import os

WTF_CSRF_ENABLED = True
##SECRET_KEY = '1BCDEFGHIJKLMNOPQRSTUVWXYZ12345'


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

class Config:
    SECRET_KEY = '1BCDEFGHIJKLMNOPQRSTUVWXYZ12345'
    MAIL_SERVER ='smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS','true').lower() in \
                   ['true','on','1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAI_PASSWORD = os.environ.get("MAIL_PASSWORD")
    FLASK_MAIL_SUBJECT_PREFIX='[Flasky]'
    FLASKY_MAIL_SENDER = 'FLASKY Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

config ={
    'default':DevelopmentConfig
}'''