tarefas = ['estudar', 'revisar']
print(tarefas)
#como inserir um item dentro de uma lista
tarefas.append('praticar')
print(tarefas)
#como inserir varios itens dentro de uma lista, usando outra lista
tarefas.extend(['testar', 'documentar'])
print(tarefas)
#eu consigo inserir um item em uma determinada posição
tarefas.insert(1,'planejar')
print(tarefas)
#remover o ultimo ite da lista
ultima = tarefas.pop()
print(tarefas)
#remover um objeto especifico
tarefas.romve('revisar')
print(tarefas)
