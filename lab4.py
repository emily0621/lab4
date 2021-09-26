from flask import Flask

lab4 = Flask(__name__)


@lab4.route('/api/v1/hello-world-2')
def helloWorld():
    return 'Hello World 2'


if __name__ == '__main__':
    lab4.run(debug=True)
