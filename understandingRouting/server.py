from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def greeting(name):
    return f"Hello {name}!"

@app.route('/say/<int:num>/<string:str>')
def repeat(num, str):
    return str * num

if __name__ == "__main__":
    app.run(debug=True)