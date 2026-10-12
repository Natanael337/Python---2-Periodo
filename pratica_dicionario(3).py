estoque = {
    'teclado': 15,
    'mouse': 20,
    'monitor': 8,
    'notebook': 5
}
estoque['webcam'] = 10
estoque['mouse'] = 25
estoque.pop('monitor')

for produto, quantidade in estoque.items():
    print('Produto: {} | Quantidade: {}'.format(produto, quantidade))

total = sum(estoque.values())
print('Itens Disponíveis no Estoque: {}'.format(total))
