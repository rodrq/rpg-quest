from openai import OpenAI
from api.src.config.settings import OPENAI_API_KEY, OPENAI_ORG_ID

client = OpenAI(api_key=OPENAI_API_KEY, organization = OPENAI_ORG_ID)
