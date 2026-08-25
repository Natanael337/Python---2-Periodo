peso = float(input('Informe o Peso da Encomenda: '))
dist = float(input('Informe a Distância em Quilômetros: '))
tipo = input('Informe o Tipo de Entrega: ').lower()
assinante = input('O Cliente é Assinante? ').lower()
valor = float(input('Informe o Valor da Compra: R$'))

taxap = peso * 2.50
print('Taxa por Peso: R$2.50 X PESO = R${:.2f}'.format(taxap))

taxad = dist * 0.30
print('Taxa por Distância: R$0.30 X DISTÂNCIA = R${:.2f}'.format(taxad))

taxab = taxad + taxap

if peso > 30:
    taxab = taxab + 80
    print('Peso do Produto Maior que 30Kg: Adicional Fixo de R$80!')

if dist > 500:
    taxab = taxab + 100
    print('Distância da Entrega Maior que 500Km: Adicional Fixo de R$100!')

if tipo == 'urgente':
    adicional = taxab * 0.60
    taxab = taxab + adicional
    print('Entrega Urgente: Adicional de 60%! - R${:.2f}'.format(adicional))
elif tipo == 'expressa':
    adicional = taxab * 0.30
    taxab = taxab + adicional
    print('Entrega Expressa: Adicional de 30%! - R${:.2f}'.format(adicional))
elif tipo == 'normal':
    print('Entrega Normal: Sem Adicional!')
else:
    print('Tipo de Entrega Inválido!')

if assinante in ['sim', 's'] and valor >= 2000 and tipo == 'normal' and peso <= 10:
    print('Cliente Assinante \nPeso Menor ou Igual a 10Kg \nCompra Igual ou Superior a R$2000 \nEntrega Normal')
    print('FRETE GRATUITO!')  # Fechamento do parêntese corrigido
    valorf = 0.0
else:
    desconto = 0.0

    if assinante in ['sim', 's']:
        desconto += 0.15
    if valor > 1000:
        desconto += 0.10

    if desconto > 0.20:
        desconto = 0.20
    valorf = taxab - (taxab * desconto)

print('Valor Final do Frete: R${:.2f}'.format(valorf))
