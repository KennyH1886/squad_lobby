# squad_lobby
# init ai framework
```python

pip install -q openai
from openai import OpenAI
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a Capital One budget virtual assistant. You are part of the 'Breaking the Piggy Bank, Reviving Personal Budgeting in the Virtual World' event. Be helpful and kind. This is for CS students, so use emojis when needed."
        },
        {
            "role": "user",
            "content": input("Ask your budget question.")
        }
    ],
    model="gpt-4o-mini",
)
response = chat_completion.choices[0].message.content
print(response)
```
