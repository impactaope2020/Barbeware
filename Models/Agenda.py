from datetime import datetime, timedelta
import sqlite3

class Agenda:
    with sqlite3.connect('Agenda') as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists Agenda(
            id integer primary key autoincrement,
            nome_cliente varchar(20),
            sobrenome_cliente varchar(40),
            email_cliente varchar(50),
            horario_marcado varchar(15)
        )""")
    
    def Agendamento(nome_cliente, sobrenome_cliente, email_cliente, horario_marcado):
        with sqlite3.connect('Agenda') as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Agenda (nome_cliente, sobrenome_cliente, email_cliente, horario_marcado)
                            values (?, ?, ?, ?)""", (nome_cliente, sobrenome_cliente, email_cliente, horario_marcado))
    
    def ConfigAgenda(horario_funcionamento, horario_fechamento, tempo_corte):
        horario_funcionamento = datetime.strptime(horario_funcionamento, "%H:%M")
        horario_fechamento = datetime.strptime(horario_fechamento, "%H:%M")
        config = [horario_funcionamento]
        while horario_funcionamento < horario_fechamento:
            config.append(horario_funcionamento + timedelta(minutes=tempo_corte))
            horario_funcionamento = horario_funcionamento + timedelta(minutes=tempo_corte)
        return config
