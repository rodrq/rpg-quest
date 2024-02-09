from starlette.config import Config

import os

basedir = os.path.abspath(os.path.dirname(__file__))


config = Config('.env')

DB_URL = config('DB_URL')
OPENAI_API_KEY = config('OPENAI_API_KEY')
OPENAI_ORG_ID = config('OPENAI_ORG_ID')
SECRET_KEY=config('SECRET_KEY')
ALGORITHM=config('ALGORITHM')
TOKEN_LIFETIME_MINUTES=config('TOKEN_LIFETIME_MINUTES')
