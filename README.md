# THE WAY – Aplicação de Gestão

Esta aplicação descreve a estrutura de base de dados no Airtable e as automatizações no Make.com para gerir serviços de Crédito, Seguro, Legalização e Consultoria.

## 1. Base de Dados no Airtable

Crie uma base chamada **"THE WAY – Base Principal"** com as seguintes tabelas e campos (otimizados para integrações e filtros no Make):

### Clientes
- **Nome** (Texto curto)
- **Email** (Email)
- **Telemóvel** (Número)
- **Tipo de Serviço** (Múltipla seleção: Crédito, Seguro, Legalização, Consultoria)
- **Último contacto** (Data)
- **Próxima ação** (Data)
- **Observações internas** (Texto longo)
- **RGPD aceite** (Sim/Não)
- **Documentos** (Anexo)
- **Créditos** (Ligação a "Créditos")
- **Seguros** (Ligação a "Seguros")
- **Consultorias** (Ligação a "Consultorias")
- **Legalizações** (Ligação a "Legalizações")

### Créditos
- **Cliente** (Ligação a "Clientes")
- **Valor (€)** (Moeda)
- **Prazo (meses)** (Número)
- **Data de realização** (Data)
- **Financeira** (Ligação a "Financeiras")
- **Fornecedor** (Ligação a "Fornecedores")
- **Comissão financeira (€)** (Moeda)
- **Comissão fornecedor (€)** (Moeda)
- **Documentos em falta?** (Sim/Não)
- **Pendente criado?** (Ligação a "Pendentes")
- **Crédito realizado?** (Sim/Não)

### Seguros
- **Cliente** (Ligação a "Clientes")
- **Tipo de seguro** (Seleção: Auto, Vida, Saúde, etc.)
- **Valor do prémio (€)** (Moeda)
- **Data de renovação** (Data)
- **Companhia** (Texto curto)
- **Freelance?** (Sim/Não)
- **Comercial responsável** (Ligação a "Comerciais")

### Consultorias
- **Cliente** (Ligação a "Clientes")
- **Tipo de serviço** (Texto curto)
- **Valor por sessão (€)** (Moeda)
- **Sessão marcada** (Data)
- **Observações** (Texto longo)

### Legalizações
- **Cliente** (Ligação a "Clientes")
- **Tipo de viatura** (Texto curto)
- **Valor total (€)** (Moeda)
- **IMT incluído?** (Sim/Não)
- **Data legalização** (Data)
- **Fornecedor** (Ligação a "Fornecedores")
- **Observações** (Texto longo)

### Fornecedores
- **Nome**
- **Email**
- **Telefone**
- **Créditos associados** (Ligação a "Créditos")
- **Legalizações associadas** (Ligação a "Legalizações")

### Financeiras
- **Nome**
- **Email**
- **Créditos associados** (Ligação a "Créditos")
- **Volume anual** (Rollup dos créditos realizados)

### Pendentes
- **Crédito** (Ligação a "Créditos")
- **Fornecedor** (Ligação automática via crédito)
- **Data de criação** (Data)
- **Dias em atraso** (Fórmula: `DATETIME_DIFF(TODAY(), {Data de criação}, 'days')`)
- **Resolvido?** (Sim/Não)

### Comerciais
- **Nome**
- **Email**
- **Créditos realizados** (Ligação a "Créditos")
- **Seguros fechados** (Ligação a "Seguros")
- **KPIs** (Rollups de número de créditos, volume total e número de seguros)

## 2. Automatizações no Make.com

1. **🎉 Aniversários**
   - **Trigger:** Airtable → campo "Faz anos hoje?" = TRUE
   - **Ação:** Enviar e‑mail via SMTP `geral@theway.com.pt` com a mensagem de parabéns.

2. **📩 Boas‑vindas a novo cliente**
   - **Trigger:** Novo cliente na tabela "Clientes".
   - **Condição:** "RGPD aceite" = TRUE
   - **Ação:** Enviar e‑mail de boas‑vindas com explicação dos serviços.

3. **⚠️ Alerta de pendentes com mais de 15 dias**
   - **Trigger:** Registos em "Pendentes".
   - **Filtro:** `{Resolvido?} = FALSE` e `{Dias em atraso} > 15`
   - **Ação:**
       - Enviar e‑mail ao fornecedor com alerta.
       - Enviar cópia para `theway.since2024@gmail.com`.
       - Atualizar o campo "Último alerta enviado" com a data atual.

4. **🔁 Renovação de seguro**
   - **Trigger:** Campo "Data de renovação" igual a hoje + 15 dias.
   - **Ação:** Enviar e‑mail ao cliente com lembrete e botão WhatsApp.

5. **📊 Geração de relatórios mensais**
   - **Trigger:** Uma vez por mês.
   - **Ação:**
       - Criar relatório com créditos por financeira, seguros por fornecedor, volume total e pendentes.
       - Exportar para PDF ou Google Docs e enviar ao administrador.

## 3. Requisitos Finais

- Todo o conteúdo em português de Portugal.
- Design minimalista com logótipo da marca.
- Compatível com integração futura no Glide.
- Estrutura preparada para assinatura digital.
- Administradores podem editar qualquer registo; comerciais apenas veem os seus próprios dados.

### Exportação para CSV/JSON

O script `export_airtable.py` gera ficheiros `csv` e `json` com a estrutura de todas as tabelas para facilitar a importação inicial no Airtable.

```bash
python export_airtable.py
```

Os ficheiros serão guardados na pasta `export/`.

