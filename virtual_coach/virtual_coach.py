import openai

openai.api_key = 'YOUR_API_KEY'

def ask_coach(query):
    response = openai.Completion.create(
      engine="gpt-3.5-turbo",
      prompt=f"Provide coaching advice on: {query}",
      max_tokens=150
    )
    return response.choices[0].text.strip()

# Usage
# print(ask_coach("How to improve my sprinting technique?"))
