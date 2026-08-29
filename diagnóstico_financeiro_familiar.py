renda = float(input('Informe a Renda Mensal da Família: R$'))
moradia = float(input('Informe o Valor dos Gastos com Moradia: R$'))
alimentacao = float(input('Informe o Valor dos Gastos com Alimentação: R$'))
transporte = float(input('Informe o Valor dos Gastos com Trasporte: R$'))
saude = float(input('Informe o Valor dos Gastos com Saúde: R$'))
educacao = float(input('Informe o Valor dos Gastos com Educação: R$'))
lazer = float(input('Informe o Valor dos Gastos com Lazer: R$'))
dividas = float(input('Informe o Valor dos Gastos com Dividas: R$'))

despesas = moradia + alimentacao + transporte + saude + lazer + dividas + educacao
saldo = renda - despesas
percentualr = despesas / renda * 100
percentuald = dividas / renda * 100

if despesas > renda and saldo < (renda * 0.20):
    print("Situação: INSOLVÊNCIA")
    print("Recomendação: Ação imediata! Renegocie dívidas urgentemente, corte todos os gastos não essenciais e busque assistência financeira.")
elif percentualr > 85 or percentuald > 35:
    print("Situação: CRÍTICA")
    print("Recomendação: Reduza gastos supérfluos drasticamente e priorize a quitação das dívidas de juros mais altos.")
elif 70 < percentualr <= 85:
    print("Situação: ATENÇÃO")
    print("Recomendação: Ajuste o orçamento familiar para criar uma margem de segurança e evitar novos parcelamentos.")
else:
    print("Situação: SAUDÁVEL")
    print("Recomendação: Excelente gestão! Continue destinando o saldo restante para investimentos e reserva de emergência.")

