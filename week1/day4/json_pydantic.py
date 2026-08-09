import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client = Groq(api_key = my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"

# structure it 
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema = Ticket.model_json_schema()
response_format = {
    "type": "json_object"
}
  
system_prompt = f"""
Extract the personal information from the ticket on strictly based on this schema and give me a json output.
{schema}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}
text = "hello My name " \
"is Hammad. I have an iphone which is not working at all. My address is Lucknow. My email is abc@gmail. My phone number is 82134"
prompt = f"""
This is a cutomer ticket. please extract the personal information from this.
{text}
"""


# message me role and content rehta
message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
# print(response)

answer = response.choices[0].message.content
print(answer)


# isko padhte kaise hai

import json
raw_json = answer
data_file=json.loads(answer)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)
print(ticket.issue)


# Homework:
# Take a resume in pdf or word
# have hr give you a list of things like skill, experience, projects
# extract these from resume 
# match against the hr list
# generate a percentage of matching or not