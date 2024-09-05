from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Página principal."

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name="mundo"):
    return "Olá, " + name

if __name__ == '__main__':
    app.run()