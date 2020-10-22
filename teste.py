from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
from Models.Usuarios import Usuario
import datetime 
import sqlite3


<<<<<<< HEAD
texto = """A """

qtd = 0
for caracteres in texto:
    qtd += 1
print(qtd)
=======
for agendamentos in Agenda.SelectAgendamentos('2020-09-20', 2):
    print(agendamentos)
>>>>>>> 7aa8ac34c7c5ed5684c487667cf36a99300d00b5
    

'''for agendamento in Agenda.ReturneAgendamentos():
    print(agendamento)'''