import sqlite3

class Usuario:
    with sqlite3.connect('Banco.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Usuario(
                        id integer primary key autoincrement,
                        nome varchar(20) not null,
                        sobrenome varchar(20) not null,
                        email varchar(50) not null,
                        senha varchar(50) not null,
                        tipo_usuario varchar(10) not null
                        )""")
        conn.commit()
    
    def CadastrarUsuario(tipo_usuario, nome, sobrenome, email, senha):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Usuario (nome, sobrenome, email, senha, tipo_usuario)
                            values(?, ?, ?, ?, ?)""", (tipo_usuario, nome, sobrenome, email, senha))
            
    
    def ValidarUsuario(email, senha):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Usuario where email = ? and senha = ?", (email, senha,))
    
    def PesquisarUsuarioEmail(email):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Usuario where email = ?", (email,))

    def RetornarUsuarios():
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Usuario")

    def RetornarBarbeiroId(id):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("select nome || ' ' || sobrenome, id from Usuario where id = ?", (id,))
    
    def DeletarBarbeiroId(id):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("Delete from Usuario where id = ?", (id,))
    
    def RetornarTipoUsuario(id):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select tipo_usuario from  Usuario where id = ?", (id,))

            

    
    