import sqlite3

class ItensPedido:
    with sqlite3.connect("Banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists ItensPedido(
            id integer primary key autoincrement,
            id_pedido integer not null,
            id_item interger not null,
            id_cliente integer not null,
            valor_item varchar(20) not null
        )""")
    
    def InserirItens(id_pedido, id_item, id_cliente, valor_item):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into ItensPedido (id_pedido, id_item, id_cliente, valor_item)
                                values (?, ?, ?, ?)""", (id_pedido, id_item, id_cliente, valor_item))
    
    def RetornarItens(id_pedido):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("""Select p.nome_produto, i.valor_item, i.id from ItensPedido i
                                        inner join Produtos  p
                                        on i.id_item = p.id
                                         where id_pedido = ?"""
                                        , (id_pedido,))
    def DeletarItem(id_item):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute('Delete from ItensPedido where id = ?', (id_item, ))
    
    def TotalPedido(id_pedido):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute('Select sum(valor_item) from ItensPedido where id_pedido = ?', (id_pedido,))
    
    def RetornarIdProduto(id_item):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute('Select id_item from ItensPedido where id = ?', (id_item, ))
    

