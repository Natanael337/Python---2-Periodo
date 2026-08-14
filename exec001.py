nome = input('Informe o Seu Nome: ')
nascimento = int(input('Informe o Seu Ano de Nascimento: '))
atual = int(input('Informe o Ano Atual: '))
idade = atual - nascimento
print('{} possui aproximadamente {} Anos!'.format(nome, idade))
