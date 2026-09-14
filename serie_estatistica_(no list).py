menor = 99999
maior = 0
soma = 0
positivos = 0
negativos = 0
zeros = 0
pares = 0
impares = 0
qtd_numeros = int(input('Informe a Quantidade de Números: '))

for c in range (0, qtd_numeros):
    numero = int(input('Digite o Número: '))
    soma = soma + numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

media = soma / qtd_numeros
print('Maior Valor Digitado: {}'.format(maior))
print('Menor Valor Digitado: {}'.format(menor))
print('Números Positivos: {}'.format(positivos))
print('Números Negativos: {}'.format(negativos))
print('Números Zeros: {}'.format(zeros))
print('Números Pares: {}'.format(pares))
print('Números Ímpares: {}'.format(impares))
print('Soma dos Valores Digitados: {}'.format(soma))
print('Média dos Valores Digitados: {:.2f}'.format(media))



