import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), os.path.pardir, '.env')
load_dotenv(env_path, override=True)

def get_env(key):
    return os.environ.get(key)

