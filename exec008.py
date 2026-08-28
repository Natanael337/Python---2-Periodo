senha = int(input('Digite uma Senha de 4 Dígitos Inteiros: '))
c = 0
while True:
    if c >= 3:
        print('Tentativas Esgotadas, Conta Bloqueada!')
        break
    else:
        pass
        vsenha = int(input('Tentativa {} - Digite a Sua Senha: '.format(c + 1)))
        if vsenha == senha:
            print('Sua Senha está Correta!')
            break
        else:
            print('Sua Senha está Incorreta!')
            c+=1
            continue

