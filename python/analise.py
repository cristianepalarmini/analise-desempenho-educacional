import pandas as pd

# Carregar os dados
dados = pd.read_csv("dados/alunos.csv")

# Indicadores gerais
total_alunos = dados["id_aluno"].nunique()
media_notas = dados["nota"].mean()
media_frequencia = dados["frequencia"].mean()

aprovados = (dados["situacao"] == "Aprovado").mean() * 100

print("ANÁLISE DE DESEMPENHO EDUCACIONAL")
print("----------------------------------")
print(f"Total de alunos: {total_alunos}")
print(f"Média geral das notas: {media_notas:.2f}")
print(f"Frequência média: {media_frequencia:.2f}%")
print(f"Taxa de aprovação: {aprovados:.2f}%")

# Desempenho por disciplina
print("\nMÉDIA POR DISCIPLINA")
print(dados.groupby("disciplina")["nota"].mean().round(2))

# Desempenho por turma
print("\nMÉDIA POR TURMA")
print(dados.groupby("turma")["nota"].mean().round(2))
