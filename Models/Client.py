import sqlite3

class Cliente:
    with sqlite3.connect("Cliente.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Cliente(
                            id integer primary key autoincrement,
                            nome varchar(20) not null,
                            sobrenome varchar(30) not null,
                            email varchar(50) not null,
                            endereco varchar(40),
                            numero interger,
                            complemento varchar(20),
                            cidade varchar(20),
                            estado varchar(20),
                            cep varchar(9) 
                            )""")
    
    def CadastrarCliente(nome, sobrenome, email, endereco, numero, complemento, cidade, estado, cep):
        with sqlite3.connect("Cliente.db") as conn:
            cursor = conn.cursor()
            cursor.execute(""" insert into Cliente (nome, sobrenome, email, endereco, numero, complemento, cidade, estado, cep)
                                        values (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (nome, sobrenome, email, endereco, numero, complemento, cidade, estado, cep))
            
    
    def RetornarClientes():
        with sqlite3.connect("Cliente.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Cliente")
    
    def ExcluirCliente(id):
        with sqlite3.connect("Cliente.db") as conn:
            cursor = conn.cursor()
            cursor.execute("Delete from Cliente where id = ? ", (id, ))
            
        
    def LocalizarCliente(id):
        with sqlite3.connect("Cliente.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Cliente where id = ?", (id,))
    
    def AtualizarCliente(id, nome, sobrenome, email, endereco, numero, complemento, cidade, estado, cep):
        with sqlite3.connect("Cliente.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""Update Cliente set nome = ?, 
                                                sobrenome = ?,
                                                email = ?,
                                                endereco = ?,
                                                numero = ?,
                                                complemento = ?,
                                                cidade = ?,
                                                estado = ?,
                                                cep = ?
                                                where id = ?
                                                """, (nome, sobrenome, email, endereco, numero, complemento, cidade, estado, cep, id))
    
    def LocalizarClienteEmail(email):
        with sqlite3.connect("Cliente.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Cliente where email = ?", (email,))
