from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name="mundo"):
    return render_template('hello.html', received_name=name)

if __name__ == '__main__':
    app.run()