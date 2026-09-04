produtos = ['Teclado', 'Mouse', 'Monitor']

#Percorrendo uma lista pelos elementos
for produto in produtos:
    print(produto)

#enumerate() para trazer o elemento e o index
for posicao, produto in enumerate(produtos, start=1):
    print('{}. {}'.format(posicao, produto))
