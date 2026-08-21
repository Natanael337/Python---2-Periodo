idade = int(input('Digite a Sua Idade: '))
pc = input('Possui Carteira de Motorista? ').lower()

if idade >= 18 and pc == 'sim':
    print('Pode Dirigir')
else:
    print('Não Pode Dirigir!')


dia = input('Digite o dia da Semana: ').upper()

if dia == 'SÁBADO' or dia == 'DOMINGO':
    print('É Final de Semana!')
else:
    print('É Dia Útil')


sistema_bloqueado = False
print('Sistema Disponível') if not sistema_bloqueado else print('Sistema Bloqueado')
