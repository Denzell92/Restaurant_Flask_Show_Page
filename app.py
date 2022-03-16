from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

#base.html ist Grundlage fuer seite

#insert in DB etc
insertInDB = False

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Food %r>' % self.id


@app.route('/')
def sayHello():
    return render_template('index.html')

@app.route('/menu')
def showMenu():
    foods = Food.query.all()

    return render_template('menu.html', foods=foods)

if insertInDB == True:
    newFood = Food(name='Lasagne Bolognese', description='Das beste Gericht der Welt')
    db.session.add(newFood)
    db.session.commit()



if __name__ == "__main__":
    app.run(debug=True)