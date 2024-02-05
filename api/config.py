from starlette.config import Config
import os

basedir = os.path.abspath(os.path.dirname(__file__))


config = Config('.env')

DB_URL = config('DB_URL')
OPENAI_API_KEY = config('OPENAI_API_KEY')
OPENAI_ORG_ID = config('OPENAI_ORG_ID')

