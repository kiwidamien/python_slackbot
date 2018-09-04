from config import get_env

class EnvConfig(object):
    "Base configuration class"
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = get_env('SECRET')

class DevelopmentEnv(EnvConfig):
    DEBUG = True

class TestingEnv(EnvConfig):
    DEBUG = True
    TESTING = True

class ProductionEnv(EnvConfig):
    DEBUG = False
    TESTING = False

app_env = {
    'development': DevelopmentEnv,
    'testing': TestingEnv,
    'production': ProductionEnv
}
