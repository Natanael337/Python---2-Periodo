soma = 0
turma = {
    '2026001':{'nome':'Ana', 'nota': 8.5},
    '2026002':{'nome':'Bruno', 'nota': 6.0},
    '2026003':{'nome':'Carla', 'nota': 9.2},
}

for matricula, dados in turma.items():
    if(dados['nota'] >= 7):
        dados['situacao'] = 'Aprovado'
    else:
        dados['situacao'] = 'Reprovado'

    soma += dados['nota']

qtd_alunos = len(turma)
media = soma / qtd_alunos

for matricula, dados in turma.items():
    print('Matrícula: {} | Nome: {} | Nota: {} | Situação: {}'.format(matricula, dados['nome'], dados['nota'], dados['situacao']))

print('Média Geral da Turma: {:.2f}'.format(media))
