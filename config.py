

class Config(object):
    DEBUG = False
    TESTING = False
    MEMOQ_SERVER_URL = "http://memoq-new.milengo.com"
    UPLOAD_FOLDER = 'media'
    SECRET_KEY = "lasdjkfhfle8293ry"
class ProductionConfig(Config):
    pass
class DevelopmentConfig(Config):
    DEBUG = True
class TestingConfig(Config):
    pass