import random
numero = random.randint(1, 100)
numerox = 0
resultado = False
tentativas = 0
tentativasr = 0
nivel = None

print('1. Nível: Fácil - 10 Tentativas \n2. Nível: Médio - 7 Tentativas \n3. Nível: Díficil - 5 Tentativas')
opcao = int(input('Escolha uma das Opções Acima: '))

if opcao == 1:
    nivel = 'Fácil'
    tentativas_max = 10
elif opcao == 2:
    nivel = 'Médio'
    tentativas_max = 7
elif opcao == 3:
    nivel = 'Difícil'
    tentativas_max = 5

if nivel in ['Fácil', 'Médio', 'Difícil']:
    print('\nAcha que é Capaz de Adivinhar em Qual Número eu Pensei? É o que Veremos! \nEu Pensei em um Número entre 1 e 200.')
    while numero != numerox:
        if tentativas == tentativas_max:
            print('Sem Tentativas Restantes! Você Perdeu, o Número era: {}'.format(numerox))
            break
        numerox = int(input('\nEm que Número eu Pensei? '))
        if numerox > 100 or numerox < 0:
            print('\nEu Disse entre 1 e 100! Você é Burro?')
        else:
            tentativas = tentativas + 1
        if numero == numerox:
            resultado = True
            print('Parabéns! Você Acertou.')
            break
        else:
            tentativasr = tentativas_max - tentativas
            if numero > numerox:
                print('Você Errou! Tente Novamente, Você ainda Tem {} Tentativas. \nDica: O Meu Número é Maior que {}'.format(tentativasr, numerox))
            else:
                print('Você Errou! Tente Novamente, Você ainda Tem {} Tentativas. \nDica: O Meu Número é Menor que {}'.format(tentativasr, numerox))
    pontuacao = tentativasr * 1000
    print('\n-------PLACAR-------')
    if resultado == True:
        print('Resultado: Vitória!')
    else:
        print('Resultado: Derrota!')
    print('Pontuação: {}'.format(pontuacao))
    print('Tentativas: {}'.format(tentativas))
else:
    print('Opção Inválida!')

