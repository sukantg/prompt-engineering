# Chat Completion API

import openai

openai.api_key = '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'

def chat_completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message["content"]
    
prompt = f'''
Change this text inside < > as if Yoda is talking to me

<Elon Reeve Musk is a South African-born entrepreneur and business magnate known for his involvement in several groundbreaking companies.
He was born on June 28, 1971, in Pretoria, South Africa. 
He developed an early interest in technology and entrepreneurship. 
Musk attended the University of Pretoria before transferring to the University of Pennsylvania, 
where he earned dual bachelor's degrees in physics and economics.>
'''

final_response = chat_completion(prompt)
print(final_response)