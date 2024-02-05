import os
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI

load_dotenv()

model = AzureChatOpenAI(
    openai_api_key= os.environ.get("OPENAI_API_KEY"),
    azure_endpoint= os.environ.get("OPENAI_ENDPOINT"),
    openai_api_version="2023-12-01-preview",
    azure_deployment= os.environ.get("AZURE_DEPLOYMENT"),
    openai_api_type="azure",
    openai_api_base= os.environ.get("OPENAI_API_BASE")
)