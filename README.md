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
# create image
```python
response = client.images.generate(
        model="dall-e-3",
        prompt=f"generate an image for a captial one cs hackathon, depicting a diverse CS college student trying to decide how to spend or save money, decide between instant and delayed gratification. just captial one and ncat logos, no other text",
        size="1024x1024",
        quality="standard",
        n=1,
        )
image_url = response.data[0].url
print(image_url)
```
![image](gameplay_image.png)
# sample cs student income expense record 
```python
import pandas as pd
import random
# Establish the base structure
data ={
    'Month': [i for i in range(1, 13)], # assuming months are numbered 1 through 12
    'Rent': [random.randint(300, 600) for _ in range(12)],
    'Groceries': [random.randint(50, 200) for _ in range(12)],
    'Books': [random.randint(0, 120) for _ in range(12)],
    'Tuition': [random.randint(2000, 5000) if i % 6 == 0 else 0 for i in range(12)], # tuition paid twice a year
    'Entertainment': [random.randint(0, 100) for _ in range(12)],
    'Transportation': [random.randint(30, 100) for _ in range(12)],
    'Miscellaneous': [random.randint(0, 300) for _ in range(12)],
    'Work-Study Deposits': [random.randint(500, 1000) for _ in range(12)] # work-study income
}

# Populate the DataFrame
df = pd.DataFrame(data)
# Save to CSV
df.to_csv('student_expenditures.csv', index=False)
```
