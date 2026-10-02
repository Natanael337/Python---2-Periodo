#1) CONJUNTO VAZIO
vazio = set()

#2) A PARTIR DE UMA LISTA
data_scientist = set(['Python', 'R', 'SQL', 'Git'])

#3) COM CHAVES E VALORES
data_engineer = {'Python', 'Java', 'Scala', 'Git'}

print(vazio)
print(data_scientist)
print(data_engineer)

#4) CONJUNTO TESTE
teste = set(['Python', 'Python', 'SQL'])

print(teste)

#5) TRATAMENTO DE ERROS
skills = {'Python', 'SQL', ('Git','Linux')}
print(skills)
try:
    skills.add(['PowerPoint', 'Blender'])
except TypeError:
    print('Uma Lista Não Pode ser Add em um Set!')
except:
    print('Error Não Identificado!')

