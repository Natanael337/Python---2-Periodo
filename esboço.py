nomes = [9999]
precos = [9999]
maior = 0
while True:
    nomes.appends = input('Informe o Nome do Produto: ')
    precos.appends = float(input('Informe o Preço Unitário do Produto: '))
    qtd = int(input('Informe a Quantidade de Produtos Compradas: '))
    totalp = preco_uni * qtd
    totalg = totalg + totalp
    qtd_total = qtd_total + qtd
    if totalp > maior:
        maior = totalp
        maior_nome = nome
    opcao = input('Deseja Continuar Comprando? ').lower()
    if opcao == ['s', 'sim']:
        continue
    else:
        print('Compra Finalizada!')
        break
if totalg > 500:
    totalg = totalg - (totalg * 0.10)
    print('10% de Desconto Aplicado!')
elif totalg > 200 and totalg < 500:
    totalg = totalg - (totalg * 0.05)
    print('5% de Desconto Aplicado!')

print('Total da Compra: {:.2f}'.format(totalg))
print('Quantidade de Produtos: {:.2f}'.format(qtd_total))
print('Produto com Maior Valor Total: {} - {:.2f}'.format(nome,))






