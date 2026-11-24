from dotenv import load_dotenv
load_dotenv()
import os
from langchain.chat_models import init_chat_model 
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_agent


prompt = PromptTemplate.from_template("lahore k bare m 2 line likho. in roman urdu")

# model = init_chat_model(
#     "openai/gpt-oss-120b",
#     model_provider="groq"
# )

# response = model.invoke("lahore k bare m 2 line likho. in roman urdu")

# print(response.content)

# prompt = PromptTemplate.from_template("tum aik teacher ho.{topic} ko students ko asan alfaz m samjhao. in roman urdu")

# chain = prompt | model
# print(chain.invoke({"topic": "Machine Learning"}).content)

def get_weather(city:str) -> str:
    """kisi bhi seher ka mosam btata hai"""
    return f"{city} m abhi 32 digree hai or dhoop hai "

agent = create_agent(
    model= init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq"
    ),

    tools=[get_weather],
    
    system_prompt = "tum aik madadgar assistent ho"
)

result = agent.invoke({
    "messages" : [{"role": "user", "content": "lahore ka mosam kya hai?.in roman urdu"}]

})

print (result["messages"][-1].content)
    