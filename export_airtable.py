import csv
import json
from pathlib import Path

# Estrutura das tabelas e respetivos campos
TABLES = {
    "Clientes": [
        "Nome", "Email", "Telemóvel", "Tipo de Serviço",
        "Último contacto", "Próxima ação", "Observações internas",
        "RGPD aceite", "Documentos", "Créditos", "Seguros",
        "Consultorias", "Legalizações"
    ],
    "Créditos": [
        "Cliente", "Valor (€)", "Prazo (meses)", "Data de realização",
        "Financeira", "Fornecedor", "Comissão financeira (€)",
        "Comissão fornecedor (€)", "Documentos em falta?",
        "Pendente criado?", "Crédito realizado?"
    ],
    "Seguros": [
        "Cliente", "Tipo de seguro", "Valor do prémio (€)",
        "Data de renovação", "Companhia", "Freelance?",
        "Comercial responsável"
    ],
    "Consultorias": [
        "Cliente", "Tipo de serviço", "Valor por sessão (€)",
        "Sessão marcada", "Observações"
    ],
    "Legalizações": [
        "Cliente", "Tipo de viatura", "Valor total (€)",
        "IMT incluído?", "Data legalização", "Fornecedor",
        "Observações"
    ],
    "Fornecedores": [
        "Nome", "Email", "Telefone", "Créditos associados",
        "Legalizações associadas"
    ],
    "Financeiras": [
        "Nome", "Email", "Créditos associados", "Volume anual"
    ],
    "Pendentes": [
        "Crédito", "Fornecedor", "Data de criação",
        "Dias em atraso", "Resolvido?"
    ],
    "Comerciais": [
        "Nome", "Email", "Créditos realizados",
        "Seguros fechados", "KPIs"
    ],
}

EXPORT_DIR = Path("export")
EXPORT_DIR.mkdir(exist_ok=True)

# Gera ficheiros CSV e JSON para cada tabela
for table, headers in TABLES.items():
    csv_path = EXPORT_DIR / f"{table}.csv"
    json_path = EXPORT_DIR / f"{table}.json"

    # Guardar CSV vazio com cabeçalhos
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

    # Guardar JSON com lista vazia e informação de campos
    with json_path.open("w", encoding="utf-8") as f:
        json.dump({"fields": headers, "records": []}, f, ensure_ascii=False, indent=2)

print(f"Ficheiros exportados para {EXPORT_DIR.resolve()}")
