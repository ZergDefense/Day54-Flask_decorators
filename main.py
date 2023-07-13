from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a peaceful husky</p>' \
           '<img src="https://media0.giphy.com/media/k9b6CX6oZelhK/giphy.gif" width=800</img>'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye!!'


@app.route('/username/<name>')
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
