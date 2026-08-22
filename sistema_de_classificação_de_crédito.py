idade = int(input('Digite a Sua Idade: '))
salario = float(input('Informe Seu Salário: '))
divida = float(input('Informe o Valor da Divída Atual: '))
tempo_emprego = int(input('Informe o Tempo de Emprego em Mêses: '))
valor = float(input('Informe o Valor da Solicitação: '))
nparcelas = int(input('Informe a Quantidade de Parcelas: '))
comprometimento = divida/salario
vparcelas = valor/nparcelas
ncomprometimento = (divida + vparcelas)/salario

if idade >= 21 and idade <= 65:
    pass
    if salario >= 2500:
        pass
        if tempo_emprego >= 12:
            pass
            if comprometimento <= 30:
                pass
                if nparcelas <= 25:
                    print('Solicitação Aprovada!')
                else:
                    print('A Nova Parcela é Maior que a 25% do seu Salário.')
            else:
                print('Seu Comprometimento Atual é Maior que a Quantia Limite de 30% para Fazer uma Solicitação de Crédito.')
        elif tempo_emprego >= 6:
            pass
            if (comprometimento + nparcelas) <= (salario * 0.50):
                print('Solicitação Aprovada com Restrições!')
            else:
                print('A Soma do Comprometimento Atual com a Nova Parcela ultrapassa 50% do Seu Salário.')
        else:
            print('Você Não Atingiu o Tempo de Emprego Minímo para Fazer uma Solicitação de Crédito.')
    else:
        print('Seu Salário é Inferior a Quantia Necessária para Fazer uma Solicitação de Crédito.')
else:
    print('Você Não Tem a Idade Necessária para Fazer uma Solicitação de Crédito.')


print('Valor da Parcela: {:.2f}'.format(vparcelas))
print('Percentual de Comprometimento: {:.2f}%'.format(comprometimento*100))
print('Novo Percentual de Comprometimento: {:.2f}%'.format(ncomprometimento*100))









