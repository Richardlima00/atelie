import mercadopago

public_key= 'APP_USR-8e1793fa-787a-45f0-9928-e3f42694cdfd'
token= 'APP_USR-512987370436168-051710-719c377d07661282772bc77b1dadb49f-1814002099'


def criar_pagamento(itens_pedido, link):
    # Configure as credenciais
    sdk= mercadopago.SDK(token)
    # Crie um item na preferência

    #itens que ele está comprando no formato de dicionário
    itens=[]
    for item in itens_pedido:
        id_produto= item.item_estoque.produto.id
        quantidade= int(item.quantidade)
        nome_produto= item.item_estoque.produto.nome
        preco_unitario= float(item.item_estoque.produto.preco)
        itens.append({
            'id': id_produto,
            'title':nome_produto,
            'quantity': quantidade,
            'unit_price': preco_unitario,
        })

    # valor total
    payment_data= {
        'items': itens,
        'back_urls': {
            'success': link,
            'pending': link,
            'failure': link
        },
        'auto_return': 'all'
    }
    resposta= sdk.preference().create(payment_data)
    link_pagamento= resposta['response']['init_point']
    id_pagamento= resposta['response']['id']
    return link_pagamento, id_pagamento