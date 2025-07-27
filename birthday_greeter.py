"""Automated birthday greeting generator.

This script reads client data from a CSV file or from Airtable and
creates professional birthday messages using OpenAI's GPT model.

Environment variables:
- OPENAI_API_KEY: API key for OpenAI.
- CLIENT_CSV_PATH: Path to a CSV file with columns `name,email,birthdate` (birthdate in YYYY-MM-DD format).
- AIRTABLE_BASE_ID: (optional) Airtable base ID for reading records.
- AIRTABLE_TABLE_NAME: (optional) Airtable table name for reading records.
- AIRTABLE_API_KEY: (optional) API key for Airtable.
"""

from __future__ import annotations

import csv
import datetime as dt
import os
from typing import List, Dict

import openai
import requests


def load_clients_from_csv(path: str) -> List[Dict[str, str]]:
    clients: List[Dict[str, str]] = []
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get("name") and row.get("birthdate"):
                clients.append(row)
    return clients


def load_clients_from_airtable(base_id: str, table_name: str, api_key: str) -> List[Dict[str, str]]:
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {"Authorization": f"Bearer {api_key}"}
    clients: List[Dict[str, str]] = []
    offset = None
    while True:
        params = {"offset": offset} if offset else {}
        resp = requests.get(url, headers=headers, params=params, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        for record in data.get("records", []):
            fields = record.get("fields", {})
            if fields.get("name") and fields.get("birthdate"):
                clients.append(fields)
        offset = data.get("offset")
        if not offset:
            break
    return clients


def find_today_birthdays(clients: List[Dict[str, str]]) -> List[Dict[str, str]]:
    today = dt.date.today()
    result = []
    for c in clients:
        try:
            bday = dt.date.fromisoformat(c["birthdate"])
        except (ValueError, KeyError):
            continue
        if bday.month == today.month and bday.day == today.day:
            result.append(c)
    return result


def generate_message(name: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = (
        "Cria uma mensagem de aniversário profissional e simpática "
        f"para o cliente {name}."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()
    except Exception as exc:  # noqa: BLE001
        return f"Feliz aniversário, {name}!"


def main() -> None:
    csv_path = os.getenv("CLIENT_CSV_PATH")
    base_id = os.getenv("AIRTABLE_BASE_ID")
    table_name = os.getenv("AIRTABLE_TABLE_NAME")
    api_key = os.getenv("AIRTABLE_API_KEY")

    clients: List[Dict[str, str]] = []
    if csv_path and os.path.exists(csv_path):
        clients.extend(load_clients_from_csv(csv_path))

    if base_id and table_name and api_key:
        try:
            clients.extend(load_clients_from_airtable(base_id, table_name, api_key))
        except Exception:
            pass

    todays_clients = find_today_birthdays(clients)
    for client in todays_clients:
        name = client.get("name", "")
        message = generate_message(name)
        print(f"Mensagem para {name}: {message}\n")


if __name__ == "__main__":
    main()
