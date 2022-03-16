from flask import Flask

app = Flask(__name__)

@app.route('/')
def sayHello():
    return '<p>Hello, World<p>'

if __name__ == "__main__":
    app.run(debug=True)