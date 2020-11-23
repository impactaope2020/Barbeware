from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
from Models.Usuarios import Usuario
from Models.Produtos import Produtos
from Models.Cliente import Cliente
import datetime 
import sqlite3


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


