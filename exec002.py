idade = int(input('Informe a Sua Idade: '))
maior_idade = idade >= 18
if maior_idade:
    print('Você é Maior de Idade!')
else:
    print('Você é Menor de Idade!')
    
#"Minimalização de Código":

print('Você é Maior de Idade!') if maior_idade else print('Você é Maior de Idade!')
