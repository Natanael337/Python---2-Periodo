total = 0
vendas = {
    'Janeiro': 12500,
    'Fevereiro': 9800,
    'Março': 15300,
    'Abril': 11700,
    'Maio': 18400,
}

print(vendas)

for mes, valor in vendas.items():
    total += valor

qtd_meses = len(vendas)
media = total / qtd_meses
mes_maior = max(vendas, key = vendas.get)
mes_menor = min(vendas, key = vendas.get)

maior = vendas[mes_maior]
menor = vendas[mes_menor]

print('Total Vendido: R${:.2f}'.format(total))
print('Média Mensal: {:.2f}'.format(media))
print('Maior Venda: {} | RS{:.2f}'.format(mes_maior, maior))
print('Menor Venda: {} | RS{:.2f}'.format(mes_menor, menor))

vendas_acima_media = {}

for mes, valor in vendas.items():
    if valor > media:
        vendas_acima_media[mes] = valor

print('Vendas Acima da Média: {}'.format(vendas_acima_media))
