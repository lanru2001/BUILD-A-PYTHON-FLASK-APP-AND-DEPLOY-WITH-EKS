# import flask
from flask import Flask, render_template
# create an app instance
app = Flask(__name__)
# create a route /
@app.route("/")     
# define the function hello             
def my_web():
   # return "my_web" 
   return "Welcome to Azeez Temitope Olanrewaju webpage!"

@app.route("/home")
def home():
   return render_template("home.html")

# on running python app.py
if __name__ == "__main__":
   # run the flask app
   app.run()
