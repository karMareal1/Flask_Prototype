from flask import Flask

app = Flask(__name__) #Setting up the app

@app.route("/") #setting up the http address
#function for the router
def index():
    return "Hello"

#checks whether the script is being run directly and not imported as a module (helps you run it)
if __name__ == "__main__":
    app.run(debug=True)
