import sqlite3

class Pedido:
    with sqlite3.connect("Banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Pedido(
            id integer primary key autoincrement,
            id_cliente integer not null,
            id_barbeiro integer not null,
            data_pedido varchar(20) not null,
            total_pedido varchar(20) not null,
            status_pedido integer not null
        )""")

    def CriarPedido(id_cliente, id_barbeiro, data_pedido, total_pedido, status_pedido):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Pedido (id_cliente, id_barbeiro, data_pedido, total_pedido, status_pedido) values (?, ?, ?, ?, ?)
                            """, (id_cliente, id_barbeiro, data_pedido, total_pedido, status_pedido))
    
    def RetornarPedidos():
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("""Select c.nome || ' ' || c.sobrenome, u.nome || ' ' || u.sobrenome,
                                    substr(p.data_pedido, 9, 2) || substr(p.data_pedido, 5, 4) || substr(p.data_pedido, 1, 4), p.total_pedido, 
                                    p.id, c.id, p.status_pedido
                                    from Pedido p 
                                    inner join  Cliente c
                                    on p.id_cliente = c.id
                                    inner join Usuario u
                                    on p.id_barbeiro = u.id""")
    def ValorPedido(total_pedido, id_pedido):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute('update Pedido set total_pedido = ? where id = ?', (total_pedido, id_pedido,))
    
    def FinalizarPedido(id_pedido):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute('update Pedido set status_pedido =  2 where id = ?', (id_pedido, ))