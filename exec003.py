nota = float(input('Digite a Sua Nota: '))
if nota <= 5:
    print('Aprovado!')
elif nota >= 7:
    print('Recuperação...')
else:
    print('Reprovado!')
#O Código acima está errado! Pois a Ordem Estruturada do Bloco de Condição Importa para o Resultado!
#Nesse Código vc poderia colocar um "if nota <= 5 and nota < 7"

if nota < 5:
    print('Reprovado')
elif nota < 7:
    print('Recuperação...')
else:
    print('Aprovado!')
