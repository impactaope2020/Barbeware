from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
import datetime 
import sqlite3


Agenda.Agendamento(1, 2, "2020-09-18", "12:00:00", 1)


agenda =  Agenda.ReturnHorarios(2, "2020-09-18")

agenda_marcada = []
for agendados in agenda:
    agenda_marcada.append(agendados)
    
print(agenda_marcada[4])

agenda_disponivel = []
for todos in ConfigAgenda.RetornarHorarios():
    if todos[3] not in agenda_marcada[4]:
        agenda_disponivel.append(todos)

print(agenda_disponivel)
