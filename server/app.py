from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param


@app.route('/count/<int:param>')
def count(param):
    return '\n'.join(str(i) for i in range(param))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'mult':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == 'mod':
        result = num1 % num2
    else:
        return 'Invalid operation'

    return str(result)


