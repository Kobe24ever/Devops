from flask import Flask, request

app = Flask(__name__)


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    if request.method == 'GET':
        return '<h1><div id="moshe"><li>mazda</li> <li>citroen</li> <li>chevrolt</li></div></h1>'
    elif request.method == "POST":
        return "saved new car"


@app.route('/')
def my_func():
    return "hello me love"

if __name__ == '__main__':
    app.run(debug=True)






