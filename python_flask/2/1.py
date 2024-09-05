from flask import Flask


app = Flask(__name__)

@app.route('/')
def greeting():
    welcome = '<h1> Olá! </h1>'
    link = '<p><a href="user/user">Clique aqui!</a></p>'
    return welcome + link

@app.route('/user/')
@app.route('/user/<name>')
def user(name="user"):
    greeting = f'<h1> Olá, {name}!</h1>'
    instruction = '<p>Altere o nome no <em> endereço do browser </em> \
      e recarregue a página</p>'
    return greeting + instruction

if __name__ == '__main__':
    app.run(debug=True)