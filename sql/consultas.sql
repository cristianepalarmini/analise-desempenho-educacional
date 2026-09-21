-- Total de alunos
SELECT COUNT(DISTINCT id_aluno) AS total_alunos
FROM alunos;

-- Média geral das notas
SELECT AVG(nota) AS media_geral
FROM alunos;

-- Frequência média
SELECT AVG(frequencia) AS frequencia_media
FROM alunos;

-- Taxa de aprovação
SELECT
    COUNT(CASE WHEN situacao = 'Aprovado' THEN 1 END) * 100.0
    / COUNT(*) AS taxa_aprovacao
FROM alunos;

-- Média por disciplina
SELECT
    disciplina,
    AVG(nota) AS media_nota
FROM alunos
GROUP BY disciplina
ORDER BY media_nota DESC;

-- Média por turma
SELECT
    turma,
    AVG(nota) AS media_nota
FROM alunos
GROUP BY turma
ORDER BY media_nota DESC;
