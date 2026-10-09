"""
Dada a lista abaixo de pedidos com id, nome, total e status, calcule o faturamento apenas dos pagos,
quantidade por status e o nome do cliente do maior pedido pago.
"""

pedidos = [
    {'id': 1, 'cliente': 'David', 'total':300.0, 'status':'pago'},
    {'id': 2, 'cliente': 'Igor Ramon', 'total': 150.0, 'status': 'pendente'},
    {'id': 3, 'cliente': 'Caio', 'total': 900.0, 'status': 'pago'},
    {'id': 4, 'cliente': 'Agnes', 'total': 200.0, 'status': 'cancelado'}
]

"""
Use listas de dicionarios e use um dicionario para contar status
"""
