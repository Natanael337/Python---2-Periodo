produto = {
    'nome': 'Notebook',
    'preco': 4500.00,
    'estoque': 12
}

i = input('Digite a Informação Desejada: ')
print(produto.get(i, 'Informação Não Encontrada!'))
