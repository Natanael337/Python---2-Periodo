nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))
nota3 = float(input('Digite a Terceira Nota: '))
freq = float(input('Informe o Percentual de Frequência: '))
atv = int(input('Informe a Quantidade de Atividades Passadas: '))
atvc = int(input('Informe a Quantidade de Atividades Concluídas: '))
media = (nota1 + nota2 + nota3) / 3
atvp = (atv/atvc) * 100

if freq >= 75:
    pass
    if media > 5:
        pass
        if media >= 9:
            pass
            if atvp == 100:
                print('Aprovado com Excelência!')
            else:
                print('Aprovado! Não foi Aprovado com Excelência por Percentual de Atividades Concluídas Menor que 100%.')
        else:
            if media >= 7:
                pass
                if atvp >= 70:
                    print('Aprovado! Não foi Aprovado com Excelência por Média Menor que 9.')
                else:
                    print('Em Recuperação! Não foi Aprovado por Percentual de Atividades Concluídas Menor que 70%.')
            else:
                if media >= 5 and media <= 6.99:
                    print('Em Recuperação! Não foi Aprovado por Média Menor que 7.')
    else:
        print('Reprovado por Nota!')
else:
    print('Reprovado por Frequência!')
