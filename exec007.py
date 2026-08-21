idade = int(input('Digite a Sua Idade: '))
salario = float(input('Informe Seu Salário: '))
divida = float(input('Informe o Valor da Divída Atual: '))
tempo_meses = int(input('Digite o Tempo de Emprego e Mêses: '))
valor_solicitado = float(input('Informe o Valor Solicitado: '))
numero_parcelas = int(input('Informe o Número de Parcelas:'))
comprometimento = divida / salario
valor_parcela = valor_solicitado / numero_parcelas

if idade >= 21 and idade <= 65:
    pass
    if salario >= 2500:
        pass
        if tempo_meses >= 12:
            pass
            if comprometimento <= 30:
                pass
                if valor_parcela <= (salario * 0.25):
                    print('Solicitação Aprovada!')

elif idade >= 21 and idade <= 65:
    pass
    if tempo_meses >= 6:
        pass
        if (compromentimento + valor_parcela) <= (salario * 0.50):
            print('Solicitação Aprovada com Restrições...')
else:
    print('Solicitação Reprovada!')

print('Valor da Parcela: {:.2f}'.format(va))
print('Percentual Atual de Comprometimento: {:.2f}')
print('Novo Percentual de Comprometimento: {}:.2f')
print('Resultado da Análise: {:.2f}')
print('Motivo Principal da Reprovação: {:.2f}')







