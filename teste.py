from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
from Models.Usuarios import Usuario
import datetime 
import sqlite3


def tipo_cliente(id):
    for tipo in Usuario.RetornarTipoUsuario(id):
        return tipo[0]

id = 1
tipo = tipo_cliente(id)
print(tipo)
    
