from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Setting up the app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #Setting up the database
db = SQLAlchemy(app) #Initializing the database
@app.route("/") #setting up the http address
#function for the router
def index():
    return "Hello"

#checks whether the script is being run directly and not imported as a module (helps you run it)
if __name__ == "__main__":
    app.run(debug=True)
