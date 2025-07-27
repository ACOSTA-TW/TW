"""Exemplo simples de utilização da API da OpenAI.

Define a variável de ambiente ``OPENAI_API_KEY`` antes de executar.
"""

import os

from openai import OpenAI


def main() -> None:
    """Gera uma mensagem de parabéns para testar a ligação à API."""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("Defina a variável OPENAI_API_KEY para prosseguir.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": (
                    "Cria uma mensagem de parabéns profissional para um cliente da THE WAY."
                ),
            }
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
