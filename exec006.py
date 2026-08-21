opp = ['sim', 's', 'não', 'nao', 'n']
idade = int(input('Digite Sua Idade: '))
salario = float(input('Informe o seu Salário: R$'))
negativado = input('Você está Negativado(a)? ').lower().strip()
tamanho_valido = len(negativado) == 1 or len(negativado) == 3

if negativado in opp:
    pass
    if idade >= 18 and salario >= 2000 and negativado in opp:
        print('Empréstimo Disponível!')
    else:
        print('Empréstimo Negado!')
else:
    print('Opção Inválida!')
