from flask import Flask, render_template, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Setting up the app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #Setting up the database
db = SQLAlchemy(app) #Initializing the database
@app.route("/") #setting up the http address
#function for the router
def index():
    return render_template('index.html') #rendering the html file

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    #function to return a string when we add a new task
    def __repr__(self):
        return '<Task %r>' %self.id    

#checks whether the script is being run directly and not imported as a module (helps you run it)
if __name__ == "__main__":
    app.run(debug=True)
