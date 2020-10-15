from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
from Models.Usuarios import Usuario
import datetime 
import sqlite3


for agendamentos in Agenda.SelectAgendamentos('2020-09-20', 2):
    print(agendamentos)
    

'''for agendamento in Agenda.ReturneAgendamentos():
    print(agendamento)'''