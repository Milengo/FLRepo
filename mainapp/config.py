import os

class Config(object):
    DEBUG = False
    TESTING = False
    MEMOQ_SERVER_URL = os.environ.get('MEMOQ_SERVER_URL')
    SECRET_KEY = "lasdjkfhfle8293ry"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    pass
