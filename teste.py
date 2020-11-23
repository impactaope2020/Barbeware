from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
from Models.Usuarios import Usuario
from Models.EntradaEstoque import EntradaEstoque
from Models.Client import Cliente
from Models.Produtos import Produtos
import datetime 
import sqlite3



"""Cadastrar Produtos  """
Produtos.CadastrarProdutos('Navalha', '1,00')
Produtos.CadastrarProdutos('Gel', '10,00')
Produtos.CadastrarProdutos('Pomada Modeladora', '10,00')
Produtos.CadastrarProdutos('Laque', '15,00')
Produtos.CadastrarProdutos('Alisante', '45,00')
Produtos.CadastrarProdutos('Shampoo', '11,00')
Produtos.CadastrarProdutos('Condicionador', '11,00')
"""Cadastrar Clientes"""
Cliente.CadastrarCliente('Kaique', 'Lelis', 'kaique_lelis@hotmail.com', 'Rua Riga', '370', '','SÂO PAULO', 'SP', '04249-070')
Cliente.CadastrarCliente('Wilson', 'Alves', 'wilson.alves@hotmail.com', 'Rua Viera', '29', '','SÂO PAULO', 'SP', '04242-170')
Cliente.CadastrarCliente('Matheus', 'Lins', 'matheus_lins@hotmail.com', 'Rua Souza', '30', '','SÂO PAULO', 'SP', '04249-070')
Cliente.CadastrarCliente('Kaique', 'Lelis', 'Kaique_lelis@hotmail.com', 'Rua Riga', '370', '','SÂO PAULO', 'SP', '04249-070')
Cliente.CadastrarCliente('Kaique', 'Lelis', 'Kaique_lelis@hotmail.com', 'Rua Riga', '370', '','SÂO PAULO', 'SP', '04249-070')
Cliente.CadastrarCliente('Kaique', 'Lelis', 'Kaique_lelis@hotmail.com', 'Rua Riga', '370', '','SÂO PAULO', 'SP', '04249-070')
Cliente.CadastrarCliente('Kaique', 'Lelis', 'Kaique_lelis@hotmail.com', 'Rua Riga', '370', '','SÂO PAULO', 'SP', '04249-070')
