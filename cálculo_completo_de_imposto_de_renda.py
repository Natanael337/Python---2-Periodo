salario = float(input('Informe o Valor do Seu Salário Bruto: '))
qtd_dependentes = int(input('Informe o Quantidade de Dependentes: '))
valor_previdencia = int(input('Informe o Valor da Previdência: '))
valor_alimenticia = int(input('Informe o Valor da Pensão Alimentícia: '))
deducao = 250 * qtd_dependentes
calculo = salario - valor_previdencia - valor_alimenticia - deducao

if calculo <= 2500:
    aliquota = 0
elif calculo > 2500.1 and calculo <= 3500:
    aliquota = 7.5
elif calculo > 3500.1 and calculo <= 5000:
    aliquota = 15
elif calculo > 5000.1 and calculo <= 7.500:
    aliquota = 22.5
else:
    aliquota = 27.5

imposto = calculo * (aliquota/100)
lsalario = salario - valor_previdencia - valor_alimenticia - imposto

print('Salário Bruto: R${:.2f}'.format(salario))
print('Total de Deduções: R${:.2f}'.format(deducao))
print('Base de Calculo: R${:.2f}'.format(calculo))
print('Alíquota: {:.2f}%'.format(aliquota))
print('Imposto: R${:.2f}'.format(imposto))
print('Salário Liquido: R${:.2f}'.format(lsalario))


