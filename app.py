from flask import Flask, redirect, render_template, request, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) #Setting up the app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' #Setting up the database
db = SQLAlchemy(app) #Initializing the database
@app.route("/") #setting up the http address
#function for the router
def index():
    if request.method =='POST':
        task_content = request.form['content'] #getting the user input
        new_task = Todo(content=task_content) #creating a new task

        try:
            db.session.add(new_task) #try adding the task to the database
            db.session.commit() #committing the changes
            return redirect('/') #return to the home page
        except:
            return "there was an issue lil bro"
    else:  
        tasks = Todo.query.order_by(Todo.date_created).all() #querying all the tasks from the database
        return render_template('index.html', tasks=tasks) #rendering the html file

@app.route('/delete/<int : id>')
def delete(id):
    task_to_delete = Todo.quesry.get_or_404(id) #getting the task to delete or returning a 404 error if not found
    try:
        db.session.delete(task_to_delete) #deleting the task
        db.session.commit() #committing the changes
        return redirect('/') #return to the home page
    except:
        return "there was an issue lil bro"
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    

        
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
