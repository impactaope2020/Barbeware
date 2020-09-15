from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
import datetime as dt
import sqlite3

ConfigAgenda.ExcluirConfigAgenda()
ConfigAgenda.ConfigAgenda("8:00", "18:00", 60)

for horario in ConfigAgenda.RetornarHorarios():
    print(horario)
