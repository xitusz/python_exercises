from flask import Flask


app = Flask(__name__)

@app.route('/')
def greeting():
    welcome = '<h1> Olá! </h1>'
    instruction = '<p>Entre com dois números</p>'
    return welcome + instruction

@app.route('/sum/')
@app.route('/sum/<num01>/<num02>')
def sum(num01=0, num02=0):
    result = float(num01) + float(num02)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)