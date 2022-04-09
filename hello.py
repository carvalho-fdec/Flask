from flask import Flask, flash, redirect, render_template, request, session, url_for, abort


app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name} </h1>'

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('template1.html', name=name.upper())



if "__main__" == __name__:
    app.run(debug=True) 
    #app.run(host='0.0.0.0', port=80)


