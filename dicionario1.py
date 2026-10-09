produto = {
    'id': 1,
    'nome': 'Teclado',
    'preco': 150.0,
    'ativo': True
}

print(produto['nome'])

produto2 = {
    'id': 2,
    'nome': 'Mouse',
    'preco': 80.0,
}
print(produto2.get('ativo')) #None
print(produto2.get('ativo', False)) #False

produto2['ativo'] = True
print(produto2.get('ativo'))
