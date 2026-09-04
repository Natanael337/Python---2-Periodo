vendas = [1200.0, 850.0, 2300.0, 450.0, 1800.0, 3200.0, 950.0]
total_itens = len(vendas)
total_vendas = sum(vendas)
media_vendas = total_vendas / total_itens
maior_venda = max(vendas)
menor_venda = min(vendas)
acima_media = []

for venda in vendas:
    if venda > media_vendas:
        acima_media.append(venda)

print('A Média de Vendas foi de {:.2f}'.format(media_vendas))
print('A Maior Venda foi: {:.2f}'.format(maior_venda))
print('A Menor Venda foi: {:.2f}'.format(menor_venda))
print('O Total de Vendas: {:.2f}'.format(total_vendas))



