nome = input('Digite o Seu Nome: ')
nota1 = float(input('Digite a 1. Nota: '))
nota2 = float(input('Digite a 2. Nota: '))
media = (nota1 + nota2) / 2

print(f'Seu Nome é sua Média é {media}')

if media >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')

n = int(input('Digite um Número Inteiro: '))
if n % 2 == 0:
    print('O Número Digitado é Par!')
else:
    print(f'O Número Digitado é Ímpar!')

salario = float(input('Informe o Seu Salário: R$'))
aumento = float(input('Informe o Perencetual de Aumento: '))
salario = salario + salario * (aumento / 100)
print('O Salário no Próximo Mês será {:.2f}'.format(salario))
