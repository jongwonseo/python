from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>\
      <p>안녕!!!</p>\
        '
  
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
  return "Bye"

@app.route('/username/<name>/1')
def greet(name):
  return f"Hello !!!{name}!"

if __name__ == '__main__':
  app.run(debug=True)
  