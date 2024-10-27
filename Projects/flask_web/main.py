from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Rabbuni!'

@app.route('/hello')
def hi():
    return 'Hello'



if __name__ == '__main__':
    app.run(debug=True)