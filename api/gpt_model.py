import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI

load_dotenv()

model = AzureChatOpenAI(
    api_key= os.environ.get("OPENAI_API_KEY"),
    azure_endpoint= os.environ.get("OPENAI_ENDPOINT"),
    openai_api_version= os.environ.get("OPENAI_API_VERSION"),
    azure_deployment= os.environ.get("AZURE_DEPLOYMENT"),
)

