estoque = int(input('Informe a Quantidade Inicial em Estoque: '))
estoque_inicial = estoque
estoque_minimo = 0.25 * estoque
entradas = 0
saidas = 0
consultas = 0
qtd_operacoes = 0
opcao = 0
total_movimentado = 0
while opcao != 5:
    print('\n1 - Entrada de Mercadoria \n2 - Saída de Mercadoria \n3 - Consultar Estoque \n4 - Definir Estoque Mínimo \n5 - Encerrar')
    opcao = int(input('Escolha uma das Opções Acima: '))

    if estoque < estoque_minimo:
        situacao = 0
        print('\nATENÇÃO! - Estoque Abaixo da Quantidade Mínima Recomendada.')
    elif estoque > estoque_minimo:
        situacao = 1
    else:
        situacao = 2

    if opcao == 1:
        entrada = int(input('\nENTRADA DE MERCADORIAS - Informe a Quantidade de Mercadorias: '))
        if entrada <= 0:
            print('Quantidade Inválida!')
        else:
            qtd_operacoes += 1
            entradas += 1
            estoque = estoque + entrada
            total_movimentado = total_movimentado + entrada

    elif opcao == 2:
        saida = int(input('\nSAÍDA DE MERCADORIAS - Informe a Quantidade de Mercadorias: '))
        if saida <= 0 or saida > estoque:
            print('Quantidade Inválida!')
        else:
            qtd_operacoes += 1
            saidas += 1
            estoque = estoque - saida
            total_movimentado = total_movimentado + saida

    elif opcao == 3:
        qtd_operacoes += 1
        consultas = consultas + 1
        print('\nEstoque Atual: {}'.format(estoque))

    elif opcao == 4:
        estoque_minimo = int(input('\nInforme o Novo Estoque Mínimo: '))



print(f'\nEstoque Inicial: {estoque_inicial}')
print(f'Quantidade de Operações: {qtd_operacoes}')
print(f'Total Movimentado: {total_movimentado}')
print(f'Quantidade em Estoque: {estoque}')
print(f'Total de Entradas: {entradas}')
print(f'Total de Saídas: {saidas}')
print(f'Total de Consultas: {consultas}')
if situacao == 1:
    print('Situação do Estoque: POSITIVA - Acima da Quantidade Mínima!')
elif situacao == 0:
    print('Situação do Estoque: NEGATIVA - Abaixo da Quantidade Mínima!')
else:
    print('Situaçaõ do Estoque: CONTROLADA - Estoque na Quantidade Mínima!')
