def inprimir_usuario(usuario: dict):
    for chave, valor in usuario.items():
        print('{} = {}'.format(chave, valor))
def extrair_frequencia_palavras(palavras: list) -> dict:
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia
usuario = {'nome':'Natan', 'ativo': False}
usuario['ativo'] = True
usuario['perfil'] = 'admin'
usuario.update({'cidade': 'Aracaju', 'idade': 19})
usuario['palavras'] = ['python', 'SQL', 'python', 'AWS', 'python', 'SQL']
