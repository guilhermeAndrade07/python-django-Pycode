import os
from openai import OpenAI

OPENAI_API_KEY= "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"

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=200,
    )

    return response.choices[0].message.content
