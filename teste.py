from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
from Models.Usuarios import Usuario
<<<<<<< HEAD
from Models.EntradaEstoque import EntradaEstoque
from Models.Client import Cliente
from Models.Produtos import Produtos
=======
from Models.Produtos import Produtos
from Models.Cliente import Cliente
>>>>>>> 8764c4abbcf2b3bada25ccc265c1274f900e9ee6
import datetime 
import sqlite3


<<<<<<< HEAD

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
=======
'''Massa de Produtos'''
Produtos.CadastrarProdutos("Gel", '10,00')
Produtos.CadastrarProdutos("Laque", '15,00')
Produtos.CadastrarProdutos("Navalha", '1,00')
Produtos.CadastrarProdutos("Shampoo", '15,00')
Produtos.CadastrarProdutos("Condicionador", '12,00')
Produtos.CadastrarProdutos("Pomada", '10,00')
Produtos.CadastrarProdutos("Alisante", '15,00')

'''Massa de Clientes'''

Cliente.CadastrarCliente('Kaique', 'Lelis Moura', 'kaique@lelis.com', 'Rua Joaquim', '37', '', 'São Paulo', 'SP', '04249-070' )
Cliente.CadastrarCliente('Felipe', 'Misso', 'misso@felipe.com', 'Rua Amora', '07', '', 'São Paulo', 'SP', '04252-071' )
Cliente.CadastrarCliente('Matheus', 'Espindola Lins', 'matheus@espindola.com', 'Rua Gilberto', '03', '', 'São Paulo', 'SP', '04229-040' )
Cliente.CadastrarCliente('Wilson', 'Alves', 'wilson@lelis.com', 'Rua Manuel Fernandez', '32', '', 'São Paulo', 'SP', '04239-020' )
Cliente.CadastrarCliente('Arthur', 'Felix', 'arthur@felix.com', 'Rua José Antonio', '70', '', 'São Paulo', 'SP', '04148-070' )
Cliente.CadastrarCliente('Maria', 'Leite', 'maria@leite.com', 'Rua Antonio', '73', '', 'São Paulo', 'SP', '04149-040' )
Cliente.CadastrarCliente('Yohana', 'da Silva Monteiro', 'monteiro@yohana.com', 'Rua Xavier', '75', '', 'São Paulo', 'SP', '04244-050' )
Cliente.CadastrarCliente('Monica', 'Jose', 'monicaa@jose.com', 'Rua Aurelio', '39', '', 'São Paulo', 'SP', '04239-010' )

'''Massa de Usuario'''
Usuario.CadastrarUsuario('Admin', 'Kaique', 'Lelis Moura', 'kaique.moura@faculdadeimpacta.com.br', '123')
Usuario.CadastrarUsuario('Admin', 'Matheus', 'Espindola', 'matheus.espindola@faculdadeimpacta.com.br', '1010')
Usuario.CadastrarUsuario('Barbeiro', 'Wilson', 'Alves', 'wilson.alves@faculdadeimpacta.com.br', '123')
Usuario.CadastrarUsuario('Barbeiro', 'Arthur', 'Felix', 'arthur.felix@faculdadeimpacta.com.br', '123')

'''Configuração da Agenda'''


>>>>>>> 8764c4abbcf2b3bada25ccc265c1274f900e9ee6
