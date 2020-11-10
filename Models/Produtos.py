import sqlite3


class Produtos:
    with sqlite3.connect("Banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Produtos(
            id integer primary key autoincrement,
            nome_produto varchar(50) not null,
            quantidade_produto integer not null,
            valor_produto real not null
            )""")

    def CadastrarProdutos(nome_produto, quantidade_produto, valor_produto):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Produtos (nome_produto, quantidade_produto, valor_produto) values (?, ?, ?)""",
                           (nome_produto, quantidade_produto, valor_produto))

    def RetornarProdutos():
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Produtos")

    def ExcluirProdutoId(id):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("delete from Produtos where id = ?", (id,))

    def RetornarProdutoId(id):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Produtos where id = ? ", (id,))

    def AlterarProduto(nome_produto, quantidade_produto, valor_produto, id):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""update Produtos set nome_produto = ?, 
                                                quantidade_produto = ?,
                                                valor_produto = ?
                                                where id = ?""", (nome_produto, quantidade_produto, valor_produto, id))

    def AlterarQuantidade(quantidade, id_produto):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("update Produtos set quantidade_produto = ? where id = ?", (quantidade, id_produto,))
