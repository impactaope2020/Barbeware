from Models.Client import Cliente
import sqlite3

for i in Cliente.LocalizarClienteEmail("kaique_lelis@hotmail.com"):
    print(i[1])