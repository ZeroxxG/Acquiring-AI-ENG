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

def llm_ans(prompt):
    message = {
        "role": "user",
        "content": prompt
    }

    messages = [message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans = response.choices[0].message.content
    return ans

good_prompt = """
# ROLE:
You are a support assistant at mobile/laptop company
# TASK
You have to classify the issue in a category
# CONSTRAINTS
You have to classify the issue in one of these categories: Billing, Technical, Return.
# OUTPUT FORMAT
Your answer should be in one word only. The one word should be one of given categories: Billing, Technical, Return.
# EXAMPLE
For instance if a user complain says he want a refund then category is Return
# FALLBACK
If the issue is unrelated to any of the categories mentioned in constraints, then the answer should be Other
This is a user complaint:
My laptop is not working
"""

bad_prompt = """
This is a user complaint:
My laptop is not working
Classify this
"""

print(llm_ans(good_prompt))
