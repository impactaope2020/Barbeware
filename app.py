from flask import Flask, render_template, request, url_for, redirect, session, jsonify, flash
from Models.Usuarios import Usuario
from Models.Client import Cliente
from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda
from Models.Produtos import Produtos
from Models.EntradaEstoque import EntradaEstoque

app = Flask(__name__)

app.secret_key = 'a1b2c3' 


nome = None
id = None

def tipo_cliente(id):
    for tipo in Usuario.RetornarTipoUsuario(id):
        return tipo[0]

@app.route("/")
@app.route("/Login")
def IndexLogin():
    session['usuario_logado'] = None
    return render_template("Login.htm", titulo="Login")

@app.route("/", methods=["POST"])
@app.route("/Login", methods=["POST"])
def EnterLogin():
    email = request.form['email']
    senha = request.form['senha']
    if email != "" and senha != "":
        for usuario in  Usuario.ValidarUsuario(str(email), str(senha)):
            if usuario:
                session['usuario_logado'] = request.form['email']
                for nomes in Usuario.PesquisarUsuarioEmail(str(email)):
                    global nome
                    nome = nomes[1]
                    global id
                    id = nomes[0]
                return redirect(url_for("Scheduling"))
    return render_template("Login.htm", email=email, mensagem="E-mail ou Senha Invalidos!", titulo="Login", tipo_usuario=tipo_cliente(id))
        

@app.route("/Login/Home")
def HomeIndex():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('IndexLogin'))
    return render_template("Home.htm", titulo="Home Page", usuario=nome, tipo_usuario=tipo_cliente(id))

@app.route("/Login/Cadastro")
def ViewClient():
    return render_template("ViewClient.htm", titulo="Cadastrar Clientes", usuario=nome, tipo_usuario=tipo_cliente(id))

@app.route("/Login/Cadastro", methods=['POST'])
def PostClient():
    nome = request.form['nome'] 
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    endereco = request.form['endereco']
    numero = request.form['numero']
    complemento = request.form['complemento']
    cidade = request.form['cidade']
    estado = request.form['estado']
    cep = request.form['cep']
    if nome != '' and sobrenome != '':
        Cliente.CadastrarCliente(nome, sobrenome, email, endereco, numero, complemento, cidade, estado, cep)
        flash("Cliente Cadastrado com Sucesso!")
        return redirect(url_for('ViewClient')) 


@app.route("/Login/HistoricoCliente")
def HistoryClient():
    return render_template("HistoryClient.htm", titulo="Histórico de Cliente", Clientes=Cliente.RetornarClientes(), usuario=nome, tipo_usuario=tipo_cliente(id))

@app.route("/Login/HistoricoCliente/<id>")
def DeleteClient(id):
    Cliente.ExcluirCliente(id)
    return redirect(url_for("HistoryClient"))

@app.route("/Login/HistoricoClienteEditar/<id>")
def ViewAlterClient(id):
    return render_template('ViewAlterClient.htm', titulo='Alterar Cliente', Cliente=Cliente.LocalizarCliente(id), usuario=nome, tipo_usuario=tipo_cliente(id))

@app.route("/Login/HistoricoClienteEditar/<id>", methods=["POST"])
def AlterClient(id):
    nome = request.form['nome'] 
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    endereco = request.form['endereco']
    numero = request.form['numero']
    complemento = request.form['complemento']
    cidade = request.form['cidade']
    estado = request.form['estado']
    cep = request.form['cep']
    if nome != '' and sobrenome != '':
        Cliente.AtualizarCliente(id, nome, sobrenome, email, endereco, numero, complemento, cidade, estado, cep)
        return redirect(url_for('HistoryClient'))


@app.route("/Login/CadastrarUsuario")
def ViewUser():
    return render_template("ViewUser.htm", titulo="Cadastrar Barbeiro", usuario=nome, tipo_usuario=tipo_cliente(id))

@app.route("/Login/CadastrarUsuario", methods=['POST'])
def CreateUser():
    tipo_usuario = request.form['tipo_usuario']
    nome1 = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    senha = request.form['senha']
    global nome
    if senha == request.form['senha2']:
        Usuario.CadastrarUsuario(nome1, sobrenome, email, senha, tipo_usuario)
        flash("Barbeiro cadastrado com Successo!")
        return render_template("ViewUser.htm",usuario=nome, titulo="Cadastrar Barbeiro", tipo_usuario=tipo_cliente(id))
    return render_template("ViewUser.htm", mensagem='Senhas divergentes', usuario=nome, titulo="Cadastrar Barbeiro", tipo_usuario=tipo_cliente(id))


@app.route("/Exit")
def Exit():
    global nome
    nome = None
    return redirect(url_for("IndexLogin"))

@app.route("/Login/Agenda")
def HistoricScheduling():
    return render_template("HistoricScheduling.htm", titulo="Agenda", usuario=nome, agenda=Agenda.ReturneAgendamentos(), barbeiro=Usuario, nome_usuario=Usuario.RetornarUsuarios(), cliente=Cliente, tipo_usuario=tipo_cliente(id))

@app.route("/Login/Agenda/<id>")
def RemoveScheduling(id):
    Agenda.RemoveAgendamento(id)
    return redirect(url_for("HistoricScheduling"))


@app.route("/Login/Agendamento")
def Scheduling():
    return render_template("Scheduling.htm", titulo="Agendamento", usuario=nome, clientes=Cliente.RetornarClientes(), barbeiros=Usuario.RetornarUsuarios(), tipo_usuario=tipo_cliente(id))


@app.route("/Login/Agendamento/<int:barbeiro_id>/<data>")
def SchedulingBarbeiro(barbeiro_id, data):
    horarios_barbeiro = Agenda.ReturnHorarios(int(barbeiro_id), str(data))
    horarios_indisponiveis = []
    horarios_disponiveis = []
    if horarios_barbeiro:
        for indisponiveis in horarios_barbeiro:
            horarios_indisponiveis.append(indisponiveis[4])

        for todos_horarios in ConfigAgenda.RetornarHorarios(barbeiro_id):
            if todos_horarios[3] not in horarios_indisponiveis:
                horarios_disponiveis.append(todos_horarios[3])


        return jsonify({"horarios_agendados": horarios_indisponiveis }, {"horarios_disponiveis": horarios_disponiveis})
    return jsonify({"horarios_agendados": horarios_indisponiveis }, {"horarios_disponiveis": horarios_disponiveis})
     


@app.route("/Login/Agendamento", methods=["POST"])
def CreateScheduling():
    cliente_id = request.form['cliente']
    barbeiro_id = request.form['barbeiro']
    data = request.form['data']
    horario = request.form['hora']
    Agenda.Agendamento(cliente_id, barbeiro_id, str(data), horario,  1 )
    flash("Agendamento Efetuado!")
    return redirect(url_for("Scheduling"))

@app.route("/Login/Configurar Agenda")
def ConfigScheduling():
    return render_template("ConfigScheduling.htm", barbeiros=Usuario.RetornarBarbeiroId(id), titulo="Configurar Agendamento", usuario=nome, tipo_usuario=tipo_cliente(id))

@app.route("/Login/Configurar Agenda", methods=['POST'])
def ConfigSchedulingPost():
    barbeiro_id = request.form['barbeiro']
    horario_funcionamento = request.form['inicio_expediente']
    horario_fechamento = request.form['final_expendiente']
    tempo_corte = request.form['tempo_corte']

    ConfigAgenda.ConfigHorarioAgenda(str(horario_funcionamento), str(horario_fechamento), int(tempo_corte), int(barbeiro_id))
    
    return redirect(url_for('ConfigScheduling'))


@app.route("/Login/CadastrarProduto")
def CreateProduce():
    return render_template('CreateProduce.htm', titulo="Cadastrar Produto", usuario=nome, tipo_usuario=tipo_cliente(id))

@app.route("/Login/CadastrarProduto", methods=["POST"])
def RegisterProduct():
    nome_produto = request.form["nome_produto"]
    valor_produto = request.form["valor_produto"]
    Produtos.CadastrarProdutos(nome_produto, valor_produto)
    flash("Produto {} cadastrado !".format(nome_produto))
    return redirect(url_for("EnterStock"))


@app.route("/Login/Estoque")
def Stock():
    return render_template("Stock.htm", titulo="Estoque", usuario=nome, estoque=Produtos.RetornarProdutos(), tipo_usuario=tipo_cliente(id))

@app.route("/Login/Estoque/<int:id>")
def DeleteProduce(id):
    Produtos.ExcluirProdutoId(id)
    return redirect(url_for("Stock"))

@app.route("/Login/Estoque/EditarProduto/<int:id>")
def EditProduce(id):
    return render_template("EditProduce.htm", titulo="Editar Produto", usuario=nome, produtos=Produtos.RetornarProdutoId(id), tipo_usuario=tipo_cliente(id))

@app.route("/Login/Estoque/EditarProduto/<int:id>", methods=["POST"])
def SaveProduce(id):
    nome_produto = request.form["nome_produto"]
    quantidade_produto = request.form["quantidade_produto"]
    valor_produto = request.form["valor_produto"]
    Produtos.AlterarProduto(nome_produto, quantidade_produto, valor_produto, id)
    return redirect(url_for("Stock"))


@app.route("/Login/Pedido")
def CreateOrder():
    return render_template("CreateOrder.htm", titulo="Criar Pedido", usuario=nome, clientes=Cliente.RetornarClientes(), produtos=Produtos.RetornarProdutos(), barbeiros=Usuario.RetornarUsuarios(), tipo_usuario=tipo_cliente(id))


@app.route("/Login/Barbeiro")
def Barber():
    return render_template("Barber.htm", titulo="Barbeiros", usuario=nome, barbeiros=Usuario.RetornarUsuarios(), tipo_usuario=tipo_cliente(id))

@app.route("/Login/Barbeiro/<int:id>")
def DeletarBarbeiro(id):
    Usuario.DeletarBarbeiroId(id)
    return redirect(url_for("Barber"))


@app.route("/Login/Agenda/<data>/<id_barbeiro>")
def FilterScheduling(data, id_barbeiro):
    horarios_agendados = [agendamentos for agendamentos in Agenda.SelectAgendamentos(data, id_barbeiro)]
    return jsonify({'Agendamentos': horarios_agendados})


@app.route("/Login/EntradaEstoque")
def EnterStock():
    return render_template("EnterStock.htm", titulo='Entrada de Produtos ', produtos=Produtos.RetornarProdutos(), usuario=nome)


@app.route("/Login/EntradaEstoque", methods=['POST'])
def EnterStockItem():
    id_produto = request.form['produto']
    quantidade = request.form['quantidade']
    valor_pago = request.form['valor_pago']
    data = request.form['data']
    EntradaEstoque.ItemEstoque(id_produto, quantidade, valor_pago, data)

    quantidade_total = 0
    for qtd in EntradaEstoque.RetornaQuantidade(id_produto):
        quantidade_total = qtd
    
    print(quantidade_total[0])
    Produtos.AlterarQuantidade(id_produto, quantidade_total[0])
    flash("Entrada efetuada com sucesso !")
    return redirect(url_for('EnterStock'))

@app.route("/Login/ListaEntrada/<int:id>")
def ListEnterStock(id):
    return render_template('ListEnterStock.htm', usuario=nome, titulo="Entradas do Produto", entradas=EntradaEstoque.RetornarEntradas(id))

@app.route("/Login/ExcluirEntrada/<int:id_entrada>/<int:id_produto>/<int:qtd_produto>")
def DeleteEnters(id_entrada, id_produto, qtd_produto):
    quantidade_atual = [qtd for qtd in Produtos.RetornarQuantidade(id_produto)]

    atualizar_quantidade = quantidade_atual[0][0] - qtd_produto
    
    print(atualizar_quantidade)
    print(id_produto)
    Produtos.AlterarQuantidade(id_produto, atualizar_quantidade)

    
    EntradaEstoque.DeletarEntrada(id_entrada)
    return redirect(url_for('ListEnterStock', id=id_produto))

if __name__ == "__main__":
    app.run(debug=True)

