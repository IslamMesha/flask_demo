from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def say_hello():
    return 'Hello, World!'


@app.route('/hi<name>')
def say_hi(name):
    return 'Hi ' + name


# use variable rules
@app.route('/<int:one>add<int:two>')
def add(one, two):
    # Views must return a string, dict, tuple, Response instance, or WSGI callable
    return str(int(one) + int(two))


# Redirection
@app.route('/panel/<salutation>')
def say_something(salutation):
    if salutation == 'guest':
        return redirect(url_for('say_hello'))
    else:
        return redirect(url_for('say_hi', name=salutation))


@app.route('/login', methods=['GET', 'POST'])
def login():
    method = request.method
    if method == 'GET':
        username = request.args.get('username')
        return redirect(url_for('say_hi', name=username))
    else:
        # Method = POST
        username = request.form.get('username')
        return redirect(url_for('say_hi', name=username))


if __name__ == '__main__':
    app.debug = True
    # run(host, port, debug, options)
    app.run('localhost', 8000)
