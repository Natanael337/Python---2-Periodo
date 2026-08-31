tentativas = 0
senha = 2177
xsenha = 0000
opcao = 0
qtd_1 = 0
qtd_2 = 0
qtd_3 = 0
saldo = 1000
total_d = 0
total_s = 0
print('------CAIXA ELETRÔNICO------')
while senha != xsenha:
    xsenha = int(input('Digite a Sua Senha: '))
    tentativas += 1
    if tentativas < 3:
        continue
    else:
        print('Conta Bloqueada! - Limite de Tentativas Atingido.')
        break

while opcao != 5:
    print('\n1 - Consultar Saldo \n2 - Depositar \n3 - Sacar \n4 - Exibir Quantidade de Operações \n5 - Encerrar')
    opcao = int(input('Escolha uma das Opçãos Acima: '))
    if opcao == 1:
        qtd_1 += 1
        print('Saldo: R${:.2f}'.format(saldo))
    elif opcao == 2:
        qtd_2 += 1
        deposito = float(input('Valor do Depósito: R$'))
        total_d += deposito
        if deposito <= 0:
            print('Valor Inválido! Por Favor, Tente Novamente!')
        saldo = saldo + deposito
    elif opcao == 3:
        qtd_3 += 1
        saque = float(input('Valor do Saque: R$'))
        total_s += saque
        if saque <= 0 or saque > saldo:
            print('Valor Inválido! Por Favor, Tente Novamente!')
        saldo = saldo - saque
    elif opcao == 4:
        qtd_all = qtd_1 + qtd_2 + qtd_3
        print('Quantidade de Operações: {}'.format(qtd_all))
        print('Quantidade de Consultas: {}'.format(qtd_1))
        print('Quantidade de Depositos: {}'.format(qtd_2))
        print('Quantidade de Saques: {}'.format(qtd_3))
    else: 
        print('Opção Inválida! Tente Novamente.')
