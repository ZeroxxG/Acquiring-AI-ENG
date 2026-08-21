import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-20b"

knowledge_base={
    "age": "The age of Hammad is 20 years",
    "city": "He live in Lucknow"
}


def retrieve_info(question):
    question=question.lower()
    if "age" in question:
        return knowledge_base["age"]
    elif "city" in question:
        return knowledge_base["city"]
    else:
        return None
def ask_llm(question):
    context = retrieve_info(question)

    sys_prompt = f"""answer in one line only. Answer only based on this context. do not hallucinate. Context: {context}"""
    system_message = {
        "role": "system",
        "content": sys_prompt
    }
    message = {
        "role": "user",
        "content": question
    }

    messages = [system_message, message]
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


question = "Which city hammad live in?"
print(ask_llm(question))


