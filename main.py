import openai
import os

# Vai buscar a tua API Key definida como variável do ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

# Faz um pedido simples para testar se tudo funciona
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Cria uma mensagem de parabéns profissional para um cliente da THE WAY."}
    ]
)

print(response.choices[0].message["content"])
