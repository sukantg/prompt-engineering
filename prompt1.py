# Completion API

import openai

openai.api_key = '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'

def generate_text(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()


prompt = 'The spiders in australia'
result = generate_text(prompt)
print(result)
