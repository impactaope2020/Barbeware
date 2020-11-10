import sqlite3

class EntradaEstoque:
    with sqlite3.connect('Banco.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists EntradaEstoque(
                            id integer primary key autoincrement,
                            id_produto integer,
                            quantidade integer,
                            valor_pago varchar(20),
                            data_entrada varchar(20)
                            )""")
    
    def ItemEstoque(id_produto, quantidade, valor_pago, data_entrada):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into EntradaEstoque (id_produto, quantidade, valor_pago, data_entrada) values(?, ?, ?, ?)"""
                                , (id_produto, quantidade, valor_pago, data_entrada))
    
    def RetornaQuantidade(id_produto):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("Select sum(quantidade) from EntradaEstoque where id_produto = ?", (id_produto,))

    def RetornarEntradas(id_produto):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("""Select a.id, b.nome_produto, a.quantidade, a.valor_pago,
                                         a.data_entrada, a.id_produto from EntradaEstoque a inner join Produtos b
                                          on a.id_produto = b.id  where id_produto = ?""", (id_produto,))
    
    def DeletarEntrada(id):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute('Delete from EntradaEstoque where id = ?', (id,))