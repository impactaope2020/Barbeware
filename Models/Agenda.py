from datetime import datetime, timedelta
import sqlite3

class Agenda:
    with sqlite3.connect('Agenda.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Agenda(
            id integer primary key autoincrement,
            nome_cliente varchar(20),
            barbeiro varchar(20),
            horario_marcado varchar(20)
        )""")
    
    def Agendamento(nome_cliente, barbeiro, horario_marcado):
        with sqlite3.connect('Agenda.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Agenda (nome_cliente, barbeiro, horario_marcado)
                            values (?, ?, ?)""", (nome_cliente, barbeiro,  horario_marcado))
    
    def RemoveAgendamento(id):
        with sqlite3.connect('Agenda.db') as conn:
            cursor = conn.cursor()
            cursor.execute("delete from Agenda where id = ?", (id,))

    def ReturneAgendamentos():
        with sqlite3.connect('Agenda.db') as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from Agenda")
    
    def ConfigAgenda(horario_funcionamento, horario_fechamento, tempo_corte):
        horario_funcionamento = datetime.strptime(horario_funcionamento, "%H:%M")
        horario_fechamento = datetime.strptime(horario_fechamento, "%H:%M")


        config = [str(horario_funcionamento)[11:].replace(":", "")]
        
        while horario_funcionamento < horario_fechamento and horario_funcionamento + timedelta(minutes=tempo_corte) < horario_fechamento:
            soma_horas = horario_funcionamento + timedelta(minutes=tempo_corte)
            horario_funcionamento = horario_funcionamento + timedelta(minutes=tempo_corte)
            config.append(str(soma_horas)[11:].replace(":", ""))
        return config
