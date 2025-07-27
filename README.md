# TW Utilities

This repository contains small utilities built with Python.

## Birthday Greeter

`birthday_greeter.py` gera mensagens de aniversário de forma automática. Os dados podem vir de um ficheiro CSV ou de uma tabela no Airtable.

### Variáveis de Ambiente

- `OPENAI_API_KEY` &ndash; chave da API do OpenAI.
- `CLIENT_CSV_PATH` &ndash; caminho para um CSV com as colunas `name`, `email` e `birthdate`.
- `AIRTABLE_BASE_ID`, `AIRTABLE_TABLE_NAME`, `AIRTABLE_API_KEY` &ndash; credenciais para leitura opcional de dados no Airtable.

### Execução

```bash
python birthday_greeter.py
```

Serão impressas mensagens para os aniversários que ocorram no dia em que o script é executado.
