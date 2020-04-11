import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base config"""
    DEBUG = True
    DB_SERVER = '0.0.0.0'
    ENV = 'development'

    @property
    def DATABASE_URI(self):
        return 'postgresql://flask_server:12345@{}/videocommunity'.format(self.DB_SERVER)
