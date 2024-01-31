from gpt_model import model
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a gamemaster of a RPG game. "
                    "Your task is to create an original and very short and concise quest \
                    for the player using the information they tell you about themselves. \
                    Don't greet the player."),

        ("human", "Hello gamemaster, I use a {weapon} as a weapon. I'm currently in the {map}"),
    ]
)

chain = LLMChain(llm=model, prompt=chat_template)

with get_openai_callback() as cb:
    response = chain.run(weapon="sword", map="beach")
    print(response)
    print(f"Total Cost (USD): ${format(cb.total_cost, '.6f')}")