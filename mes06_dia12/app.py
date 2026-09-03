from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
from model.usuario import Usuario
from model.livro import Livro

app = Flask(__name__)
app.secret_key = "chave_secreta_super_segura"

# Inicializar Tabelas do Banco
Usuario.criar_tabela()
Livro.criar()

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        usuario = Usuario.autenticar(login, senha)

        if usuario:
            session['usuario'] = usuario['login']
            return redirect(url_for('dashboard'))
        else:
            flash("Usuário ou senha incorretos!", "danger")
    else:
        return render_template('login.html')
    
@app.route('/register', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']

        if Usuario.cadastrar(login, senha):
            flash("Usuário registrado com sucesso! Faça login.", "sucess")
            return redirect(url_for('login'))
        else:
            flash("Erro ao registrar ou usuário já existe", "danger")
    return render_template('registrar.html')       

@app.route('/dasboard')
def dashboard():
    if  'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', usuario=session['usuario'])

@app.route('/livro/cadastrar', methods=['GET', 'POST'])
def cadastrar_livro():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        Livro.inserir(
            titulo=request.form['titulo'],
            autor1=request.form['autor1'],
            autor2=request.form['autor2'],
            autor3=request.form['autor3'],
            isbn=request.form["isbn"],
            assunto=request.form['assunto'],
            edicao=request.form['edicao'],
            editora=request.form['editora'],
            ano=request.form['ano']
        )
        flash("Livro cadastrado com sucesso!", "sucess")
        return redirect(url_for('consultar_livros'))
    
    return render_template('cadastrar_livros.html')

@app.route('/livros/consultar')
def consultar_livros():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    lista_livros = Livro.consultar()
    return render_template('consultar_livros.html', livros=lista_livros)

@app.route('/livros/excluir/<int:id_livro>')
def excluir_livro(id_livro):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    Livro.excluir(id_livro)
    flash("Livro removido com sucesso!", "sucess")
    return redirect(url_for('consultar_livros'))

@app.route('/livros/exportar')
def exportar_excel():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    try:
        caminho_arquivo = Livro.exportar()
        return send_file(caminho_arquivo, as_attachment=True)
    except Exception as e:
        flash(f"Erro ao exportar: {e}", "danger")
        return redirect(url_for('consultar_livros'))
    
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)