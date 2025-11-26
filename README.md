# python-routing-and-views-lab

🔹 1. Import Flask
from flask import Flask


You bring in the Flask class so you can create a web application.

🔹 2. Create the Flask App
app = Flask(__name__)


app is your website/server.

__name__ tells Flask where to find files and resources.

 3. Home Route – “/”
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

✔ What it does:

When you visit:
http://localhost:5555/

It displays the message:
Python Operations with Flask Routing and Views

@app.route('/') tells Flask that this is the function for the home page.

4. Print Any String – /print/<string:param>
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

✔ What happens:

Example:
/print/Elijah

It prints "Elijah" on your terminal.

It also shows "Elijah" in the browser.

The <string:param> part means the URL must contain a string.

 5. Count Numbers – /count/<int:param>
@app.route('/count/<int:param>')
def count(param):
    return '\n'.join(str(i) for i in range(param))

✔ What happens:

Example:
/count/5

This creates numbers from 0 to 4:

0
1
2
3
4


range(param) generates the numbers.

'\n'.join() puts each number on a new line.

6. Math Operations – /math/<num1>/<operation>/<num2>
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

✔ How to use it:

You put:

/math/<number1>/<operation>/<number2>

✔ Examples:
URL	Operation	Result
/math/10/add/5	10 + 5	15
/math/20/sub/7	20 - 7	13
/math/6/mult/3	6 × 3	18
/math/9/div/3	9 ÷ 3	3.0
/math/10/mod/4	10 % 4	2

If someone uses an operation you did not define, the code returns:

Invalid operation

7. Run the Server
if __name__ == '__main__':
    app.run(port=5555, debug=True)

✔ What this means:

This code runs only if you run the file directly, not if imported.

port=5555 → your website runs on:
http://localhost:5555

debug=True:

auto-restarts when you edit code

shows error messages for debugging