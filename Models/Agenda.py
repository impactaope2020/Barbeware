import sqlite3

class Agenda:
    with sqlite3.connect("Agenda.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Agenda(
                            id integer primary key autoincrement not null,
                            agenda_codcliente integer key not null,
                            agenda_codbarbeiro integer not null,
                            agenda_data date not null,
                            agenda_horario time not null)""")
        
    def  AgendarCliente(agenda_codcliente,  agenda_codbarbeiro, agenda_data,  agenda_horario):
        with sqlite3.connect("Agenda.db") as conn:
            cursor = conn.cursor()
            cursor.execute(""" insert into Agenda(agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario) values(?, ?, ?, ?)""", (agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario))
            conn.commit
            
    def ListarAgendamento():
        with sqlite3.connect("Agenda.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Agenda")
        
    def ExcluirAgendamento(id):
        with sqlite3.connect("Agenda.db") as conn:
            cursor = conn.cursor()
            cursor.execute("Delete from Agenda where id = ? ", (id, ))
            conn.commit()

    def Reagendamento(agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario):
        with sqlite3.connect("Agenda.db") as conn:
            cursor = conn.cursor()
            cursor.execute(""" Update Agenda set agenda_data = ?, agenda_horario = ?
                                                where id = ? """, (agenda_codcliente, agenda_codbarbeiro, agenda_data, agenda_horario, id))