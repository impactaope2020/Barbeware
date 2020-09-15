from datetime import datetime, timedelta
import sqlite3

class ConfigAgenda:
    with sqlite3.connect("ConfigAgenda.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists ConfigAgenda(
            horario_inicio varchar(8),
            horario_final varchar(8),
            tempo_corte varchar(3)
        )""")

    def CadastrarConfigAgenda(horario_funcionamento, horario_fechamento, tempo_corte):
        with sqlite3.connect("ConfigAgenda.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""Insert into ConfigAgenda values (?, ?, ?)""", (horario_funcionamento, horario_fechamento, tempo_corte))
    
    def RetornarHorarios():
        with sqlite3.connect("ConfigAgenda.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from ConfigAgenda ")
    
    def ExcluirConfigAgenda():
        with sqlite3.connect("ConfigAgenda.db") as conn:
            cursor = conn.cursor()
            cursor.execute("delete from ConfigAgenda")


    def ConfigHorarioAgenda(horario_funcionamento, horario_fechamento, tempo_corte):
        if horario_fechamento == "" or  horario_fechamento == "" or tempo_corte == "":
            return "Todos os Campos são obrigatorios"

        horario_funcionamento = datetime.strptime(horario_funcionamento, "%H:%M")
        horario_fechamento = datetime.strptime(horario_fechamento, "%H:%M")
        
        ConfigAgenda.ExcluirConfigAgenda()
        ConfigAgenda.CadastrarConfigAgenda(horario_funcionamento, horario_fechamento, tempo_corte)

        while horario_funcionamento < horario_fechamento and horario_funcionamento + timedelta(minutes=tempo_corte) <= horario_fechamento:
            soma_horas = horario_funcionamento + timedelta(minutes=tempo_corte)
            horario_funcionamento = horario_funcionamento + timedelta(minutes=tempo_corte)
            ConfigAgenda.CadastrarConfigAgenda(horario_funcionamento, horario_fechamento, tempo_corte)
        
        
    

