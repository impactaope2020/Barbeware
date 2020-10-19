from datetime import datetime, timedelta
import sqlite3

class ConfigAgenda:
    with sqlite3.connect("Banco.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create table if not exists ConfigAgenda(
            id_config integer primary key autoincrement,
            horario_inicio varchar(8),
            horario_final varchar(8),
            intervalo varchar(8),
            tempo_corte varchar(3),
            status integer
        )""")

    def CadastrarConfigAgenda(horario_funcionamento, horario_fechamento, intervalo, tempo_corte, status):
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""Insert into ConfigAgenda(horario_inicio, horario_final, intervalo,  tempo_corte, status) values (?, ?, ?, ?, ?)""", (horario_funcionamento, horario_fechamento, intervalo, tempo_corte, status))
    
    def RetornarHorarios():
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("select * from ConfigAgenda where status = 1")
    
    def StatusConfig():
        with sqlite3.connect("Banco.db") as conn:
            cursor = conn.cursor()
            cursor.execute("update ConfigAgenda set status = 2 ")


    def ConfigHorarioAgenda(horario_funcionamento, horario_fechamento, tempo_corte):
        if horario_fechamento == "" or  horario_fechamento == "" or tempo_corte == "":
            return "Todos os Campos são obrigatorios"
        

        horario_funcionamento = datetime.strptime(horario_funcionamento, "%H:%M")
        horario_fechamento = datetime.strptime(horario_fechamento, "%H:%M")


        soma_horas = str(horario_funcionamento)[11:]
        print(soma_horas)        
        ConfigAgenda.StatusConfig()
        ConfigAgenda.CadastrarConfigAgenda(horario_funcionamento, horario_fechamento, soma_horas, tempo_corte, 1)

        soma_horas = datetime.strptime(soma_horas, "%H:%M:%S")
        print(soma_horas)
        print(horario_fechamento)
        while soma_horas < horario_fechamento and soma_horas + timedelta(minutes=tempo_corte) <= horario_fechamento:
            soma_horas = soma_horas + timedelta(minutes=tempo_corte)
            ConfigAgenda.CadastrarConfigAgenda(horario_funcionamento, horario_fechamento, str(soma_horas)[11:], tempo_corte, 1)
            
        
        
    

