from flask import Flask, render_template, request, url_for, redirect, session
from Models.Usuarios import Usuario
from Models.Client import Cliente
from Models.Agenda import Agenda
from Models.ConfigAgenda import ConfigAgenda

app = Flask(__name__)

app.secret_key = 'a1b2c3' 

nome = None

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
                return redirect(url_for("Scheduling"))
    return render_template("Login.htm", email=email, mensagem="E-mail ou Senha Invalidos!", titulo="Login")
        

@app.route("/Login/Home")
def HomeIndex():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('IndexLogin'))
    return render_template("Home.htm", titulo="Home Page", usuario=nome)

@app.route("/Login/Cadastro")
def ViewClient():
    return render_template("ViewClient.htm", titulo="Cadastrar Clientes", usuario=nome)

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
        return redirect(url_for('ViewClient')) 



@app.route("/Login/HistoricoCliente")
def HistoryClient():
    return render_template("HistoryClient.htm", titulo="Histórico de Cliente", Clientes=Cliente.RetornarClientes(), usuario=nome)

@app.route("/Login/HistoricoCliente/<id>")
def DeleteClient(id):
    Cliente.ExcluirCliente(id)
    return redirect(url_for("HistoryClient"))

@app.route("/Login/HistoricoClienteEditar/<id>")
def ViewAlterClient(id):
    return render_template('ViewAlterClient.htm', titulo='Alterar Cliente', Cliente=Cliente.LocalizarCliente(id), usuario=nome)

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
    return render_template("ViewUser.htm", titulo="Cadastrar Barbeiro", usuario=nome)

@app.route("/Login/CadastrarUsuario", methods=['POST'])
def CreateUser():
    nome1 = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    senha = request.form['senha']
    global nome
    if senha == request.form['senha2']:
        Usuario.CadastrarUsuario(nome1, sobrenome, email, senha)
        return redirect(url_for("ViewUser"))
    return render_template("ViewUser.htm", mensagem='Senhas divergentes', usuario=nome, titulo="Cadastrar Barbeiro")


@app.route("/Exit")
def Exit():
    global nome
    nome = None
    return redirect(url_for("IndexLogin"))


@app.route("/Login/Agenda")
def HistoricScheduling():
    return render_template("HistoricScheduling.htm", titulo="Agenda", usuario=nome, agenda=Agenda.ReturneAgendamentos())

@app.route("/Login/Agenda/<id>")
def RemoveScheduling(id):
    Agenda.RemoveAgendamento(id)
    return redirect(url_for("HistoricScheduling"))


@app.route("/Login/Agendamento")
def Scheduling():
    return render_template("Scheduling.htm", titulo="Agendamento", usuario=nome, horarios=ConfigAgenda.RetornarHorarios(), clientes=Cliente.RetornarClientes(), barbeiros=Usuario.RetornarUsuarios())

@app.route("/Login/Agendamento", methods=["POST"])
def CreateScheduling():
    cliente = request.form['cliente']
    barbeiro = request.form['barbeiro']
    data = request.form['dia']
    horario = request.form['hora']
    data_hora = str(data) + " " + str(horario)
    Agenda.Agendamento(str(cliente), str(barbeiro), data_hora )
    return redirect(url_for("CreateScheduling"))

@app.route("/Login/Configurar Agenda")
def ConfigScheduling():
    return render_template("ConfigScheduling.htm", titulo="Configurar Agendamento", usuario=nome)

@app.route("/Login/Configurar Agenda", methods=['POST'])
def ConfigSchedulingPost():
    horario_funcionamento = request.form['inicio_expediente']
    horario_fechamento = request.form['final_expendiente']
    tempo_corte = request.form['tempo_corte']

    ConfigAgenda.ConfigHorarioAgenda(str(horario_funcionamento), str(horario_fechamento), int(tempo_corte))
    
    return redirect(url_for('ConfigScheduling'))

if __name__ == "__main__":
    app.run(debug=True)
