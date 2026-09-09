votosA = 0
votosB = 0
votosC = 0
votosD = 0
validos = 0
invalidos = 0
total = 0
opcao = 1
while opcao != 0:
    print('\n1 - Candidato A (22) \n2 - Candidato B (13) \n3 - Candidato C (14) \n4 - Candidato D (70) \n5 - Voto em Branco/Nulo \n0 - Encerrar Votação')
    opcao = int(input('Escolha uma das Opções Acima: '))

    if opcao == 1:
        votosA += 1
        validos += 1
        total = total + 1
        print('\nVoto no Candidato A (22) - Registrado!')
    elif opcao == 2:
        votosB += 1
        validos += 1
        total = total + 1
        print('\nVoto no Candidato B (13) - Registrado!')
    elif opcao == 3:
        votosC += 1
        validos += 1
        total = total + 1
        print('\nVoto no Candidato C (14) - Registrado!')
    elif opcao == 4:
        votosD += 1
        validos += 1
        total = total + 1
        print('\nVoto no Candidato D (70) - Registrado!')
    elif opcao == 5:
        invalidos += 1
        total = total + 1
        print('Voto em Branco/Nulo - Registrado!')
    else:
        print('Opção Inexistente! Por Favor, Tente Novamente!')

percentualA = votosA / 100
percentualB = votosB / 100
percentualC = votosC / 100
percentualD = votosD / 100
percentual_valido = validos / 100
percentual_invalido = invalidos / 100

print('\nVotos no Candidato A: {}'.format(votosA))
print('Votos no Candidato B: {}'.format(votosB))
print('Votos no Candidato C: {}'.format(votosC))
print('Votos no Candidato D: {}'.format(votosD))
print('Total de Votos: {}'.format(total))
print('\nPercentual de Votos Válidos: {}'.format(percentual_valido))
print('Percentual de Votos Invalidos: {}'.format(percentual_invalido))
print('Percentual de Votos no Candidato A: {}'.format(percentualA))
print('Percentual de Votos no Candidato B: {}'.format(percentualB))
print('Percentual de Votos no Candidato C: {}'.format(percentualC))
print('Percentual de Votos no Candidato D: {}'.format(percentualD))

maior_percentual = max(percentualA, percentualB, percentualC, percentualD)

vencedores = []
if percentualA == maior_percentual: vencedores.append('Candidato A')
if percentualB == maior_percentual: vencedores.append('Candidato B')
if percentualC == maior_percentual: vencedores.append('Candidato C')
if percentualD == maior_percentual: vencedores.append('Candidato D')

if maior_percentual == 0:
    print('\nNão Houveram Votos Válidos!')
elif len(vencedores) > 1:
    print('Houve um Empate entre: {}'.format(', '.join(vencedores)))
else:
    print('O Vencedor é o {}'.format(vencedores[0]))
