from flask import Flask, request


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return "Página principal."

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name):
    return "Olá, " + name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Recebeu post! Fazer login!"
    else:
        return "Recebeu get! Exibir FORM de login."

if __name__ == '__main__':
        app.run()