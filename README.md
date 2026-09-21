# 📊 Análise de Desempenho Educacional

Projeto de análise de dados desenvolvido para transformar dados acadêmicos em indicadores de desempenho, frequência e aprovação.

O projeto simula um cenário educacional e demonstra um fluxo completo de análise de dados, desde a organização da base até a criação de indicadores e visualização em dashboard.

---

## 🎯 Objetivo

Analisar o desempenho dos alunos e identificar padrões relacionados a:

- notas;
- frequência;
- aprovação;
- turmas;
- disciplinas.

A análise foi estruturada para apoiar a interpretação dos dados e facilitar a identificação de informações relevantes para acompanhamento do desempenho acadêmico.

---

## 📌 Principais indicadores

- **Total de alunos**
- **Média geral das notas**
- **Taxa de aprovação**
- **Média de frequência**
- **Média de notas por turma**
- **Média de notas por disciplina**
- **Situação dos alunos**

---

## 📊 Dashboard

O dashboard foi desenvolvido no Power BI para apresentar os principais indicadores de forma visual e facilitar a análise dos dados.

![Dashboard de Desempenho Educacional](dashboard/Dashboard%20de%20Desempenho%20Educacional.png)

---

## 🔎 Análises realizadas

### Desempenho acadêmico
Análise das médias de notas por turma e disciplina para identificar diferenças de desempenho.

### Frequência
Análise da frequência média dos alunos e sua distribuição entre as turmas.

### Situação dos alunos
Análise da quantidade de alunos aprovados e em recuperação.

### Indicadores gerais
Construção de indicadores para apresentar uma visão consolidada do desempenho educacional.

---

## 🛠️ Tecnologias utilizadas

- **Power BI** — criação do dashboard e visualização dos dados
- **Python** — análise e tratamento dos dados
- **Pandas** — manipulação da base de dados
- **SQL** — consultas e agregações
- **GitHub** — versionamento e documentação do projeto

---

## 🐍 Python

O projeto utiliza Python e Pandas para realizar análises como:

- quantidade de alunos;
- média geral das notas;
- frequência média;
- taxa de aprovação;
- média por disciplina;
- média por turma.

Arquivo:

`python/analise.py`

---

## 🗄️ SQL

Foram desenvolvidas consultas SQL para análise dos principais indicadores.

Entre as consultas estão:

- total de alunos;
- média geral;
- frequência média;
- taxa de aprovação;
- média por disciplina;
- média por turma.

Arquivo:

`sql/consultas.sql`

---

## 📁 Estrutura do projeto

```text
analise-desempenho-educacional/
│
├── dados/
│   └── alunos.csv
│
├── dashboard/
│   ├── Dashboard de Desempenho Educacional.png
│   └── LEIA-ME.txt
│
├── docs/
│   └── analise.md
│
├── python/
│   └── analise.py
│
├── sql/
│   └── consultas.sql
│
└── README.md
