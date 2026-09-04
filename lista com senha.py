#ATIVIDADE 2 - PYTHON(04/09/2026)

tipos atendimentos = ['N = Normal', 'P = Preferencial']
print(tipos atendimentos)
fila = ['N001', 'N002', 'N003']
print('Painel')
print('Senha sendo chamada: {fila[0]}')
fila.pop(0)

print('Retirar nova senha')
fila.append('N003')

for posicao, senha in enumerate(fila, start=1):
	print('{}.{}'.format(posicao, senha)

