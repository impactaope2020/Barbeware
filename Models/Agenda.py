import sqlite3

class Agenda:
    with sqlite3.connect("Banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Agenda(
            id integer primary key autoincrement,
            agenda_codcliente integer not null,
            agenda_codbarbeiro integer not null,
            agenda_data varchar(20) not null,
            agenda_horarios varchar(20) not null,
            agenda_config integer not null
        )""")
    
    def Agendamento(agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horarios, agenda_config):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Agenda (agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horarios, agenda_config)
                            values (?, ?, ?, ?, ?)""", (agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horarios, agenda_config))
    
    def RemoveAgendamento(id):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            cursor.execute("delete from Agenda where id = ?", (id,))

    def ReturneAgendamentos():
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Agenda")

    def ReturnHorarios(barbeiro, data):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Agenda where agenda_codbarbeiro = ? and agenda_data = ?", (barbeiro, data))
                            
        
    def  AgendarCliente(agenda_codcliente,  agenda_codbarbeiro, agenda_data,  agenda_horario):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute(""" insert into Agenda(agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario) values(?, ?, ?, ?)""", (agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario))
            conn.commit
            
    def ListarAgendamento():
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Agenda")
        
    def ExcluirAgendamento(id):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("Delete from Agenda where id = ? ", (id, ))
            conn.commit()

    def Reagendamento(agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute(""" Update Agenda set agenda_data = ?, agenda_horario = ?
                                                where id = ? """, (agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario, id))

    def SelectAgendamentos(data, id_barbeiro):
        with sqlite3.connect('Banco.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("""Select  Cliente.nome || ' ' || Cliente.sobrenome, Usuario.nome || ' ' || Usuario.sobrenome,
                                        agenda_horarios || ' ' || agenda_data, Agenda.id from Agenda inner Join 
                                        Usuario on Usuario.id = Agenda.agenda_codbarbeiro inner join 
                                        Cliente on Cliente.id = Agenda.agenda_codcliente
                                        where agenda_data = ? and agenda_codbarbeiro = ?
                                        """, (data, id_barbeiro))