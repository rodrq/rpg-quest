from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.callbacks import get_openai_callback

import os
load_dotenv()

model = AzureChatOpenAI(
    api_key= os.environ.get("OPENAI_API_KEY"),
    azure_endpoint= os.environ.get("OPENAI_ENDPOINT"),
    openai_api_version="2023-05-15",
    azure_deployment="gpt-4-32k",
)

prompt_template = PromptTemplate.from_template(
    "You are the admin of a RPG game. You will create a short and original quest for me. " +
    "I am a {sex} {fighting_class} that uses {weapon} as a weapon. " +
    "I am currently in {map}. In the {map} there are spiders."
)
prompt = prompt_template.format(sex="male", fighting_class="warrior", weapon="axe", map="Eastern Forest")

with get_openai_callback() as cb:
    model([prompt])
    print(
        f"Total Cost (USD): ${format(cb.total_cost, '.6f')}"
    )

    