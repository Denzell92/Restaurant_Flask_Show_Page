from flask import Flask, render_template, url_for

#base.html ist Grundlage fuer seite


app = Flask(__name__)

@app.route('/')
def sayHello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)