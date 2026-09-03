# importa a classe flask _
from flask import Flask

# importa a função render-template
from flask import render_template

# cria a aplicação flask
app = Flask(__name__)

# rota inicial 
@app.route('/')
def index():
    return render_template('index.html')

# rota pagina sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# rota página contato
@app.route('/contato')
def contato():
    return render_template('contato.html')

# rota página video
@app.route('/video')
def video():
    return render_template('video.html')

# executa o servidor flask
if __name__ == '__main__':
    app.run(debug=True,port=5000)
