maior_media = 0
menor_media = 10
melhor_aluno = ''
pior_aluno = ''
aprovados = 0
recuperacao = 0
reprovados = 0
qtd_alunos = int(input('Informe a Quantidade de Alunos: '))

for c in range(0, qtd_alunos):
    nome = input('\nInforme o Nome do Aluno: ')
    nota1 = float(input('Informe a Primeira Nota: '))
    nota2 = float(input('Informe a Segunda Nota: '))
    nota3 = float(input('Informe a Terceira Nota: '))
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        aprovados += 1

    elif media >= 5:
        recuperacao += 1

    else:
        reprovados += 1

    if media > maior_media:
        maior_media = media
        melhor_aluno = nome
    elif media < menor_media:
        menor_media = media
        pior_aluno = nome

percentual = aprovados / qtd_alunos * 100
print('\nAlunos Aprovados: {}'.format(aprovados))
print('Alunos Em Recuperação: {}'.format(recuperacao))
print('Alunos Reprovados: {}'.format(reprovados))
print('Percentual de Aprovação: {:.2f}%'.format(percentual))
print('Maior Média: {:.2f}'.format(maior_media))
print('Melhor Aluno: {}'.format(melhor_aluno))
print('Menor Média: {:.2f}'.format(menor_media))
print('Pior Aluno: {}'.format(pior_aluno))

