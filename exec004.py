numero1 = float(input('Digite um Número: '))
if numero1 < 0:
    print('O Número Digitado é Negativo!')
elif numero1 > 0:
    print('O Número Digitado é Positivo!')
else:
    print('O Número Digitado é Zero!')

if numero1 % 2 == 0:
    print('O Número Digitado é Par!')
else:
    print('O Número Digitado é Ímpar!')

numero2 = float(input('Digite Outro Número: '))
maior = numero1
if numero2 > numero1:
    maior = numero2
    print('O Maior Número entre os Digitados é {}'.format(numero2))
elif numero1 == numero2:
    print('Os Número São Iguais!')
else:
    print('O Maior Número entre os Digitados é {}'.format(numero1))

salario = float(input('Informe o Seu Salário: '))
if salario < 2000:
    aumento = salario * 0.10
    salario = salario + aumento
    print('O Valor do aumento foi de: {}'.format(aumento))
    print('O Seu novo Salário com 10% de Aumento será: {}'.format(salario))
else:
    salario = salario + (salario * 0.05)
    print('O Valor do aumento foi de: {}'.format(aumento))
    print('O Seu novo Salário com 5% de Aumento será: {}'.format(salario))
