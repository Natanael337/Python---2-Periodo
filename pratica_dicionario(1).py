aluno = {
    'nome': 'Carlos',
    'idade': 21,
    'curso': 'Sistemas de Informação',
    'nota': 7.0,
    'situacao' : 'Aprovado'
}
print('Aluno: {} \nCurso: {}'.format(aluno.get('nome'), aluno.get('curso')))

aluno['nota'] = 8.5

print(aluno)
