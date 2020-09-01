from flask import Flask, render_template, request, url_for, redirect
from Models.Usuarios import Usuario
from Models.Client import Cliente

app = Flask(__name__)

nome = None

@app.route("/")
@app.route("/Login")
def IndexLogin():
    return render_template("Login.htm", titulo="Login")

@app.route("/", methods=["POST"])
@app.route("/Login", methods=["POST"])
def EnterLogin():
    email = request.form['email']
    senha = request.form['senha']
    if email != "" and senha != "":
        for usuario in  Usuario.ValidarUsuario(str(email), str(senha)):
            if usuario:
                for nomes in Cliente.LocalizarClienteEmail(str(email)):
                    global nome
                    nome = nomes[1]
                return redirect(url_for("HomeIndex"))
    return render_template("Login.htm", email=email, mensagem="E-mail ou Senha Invalidos!", titulo="Login")
        

@app.route("/Login/Home")
def HomeIndex():
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
def ViewUsuario():
    return render_template("ViewUser.htm", titulo="Cadastrar Usuario", usuario=nome)

@app.route("/Login/CadastrarUsuario", methods=['POST'])
def CreateUser():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    datanascimento = request.form['datanascimento']
    email = request.form['email']
    senha = request.form['senha']
    Usuario.CadastrarUsuario(nome, sobrenome, datanascimento, email, senha)
    return redirect(url_for("ViewUsuario"))



if __name__ == "__main__":
    app.run(debug=True)
