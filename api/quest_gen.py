from gpt_model import model
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a gamemaster of a RPG game. "
                    "I am {name}. Your task is to create an original and very short and concise quest \
                    for the player using the information they tell you about themselves. \
                    Speak to the player directly."),

        ("human", "Hello gamemaster, I am a {class_}. I'm currently in the {map}"),
    ]
)

chain = LLMChain(llm=model, prompt=chat_template)

def generate_quest(name, class_, map):
    with get_openai_callback() as cb:
        response = chain.run(name=name, class_=class_, map=map)
        cost = cb.total_cost
        return response, cost
        #print(f"Total Cost (USD): ${format(cb.total_cost, '.6f')}")
