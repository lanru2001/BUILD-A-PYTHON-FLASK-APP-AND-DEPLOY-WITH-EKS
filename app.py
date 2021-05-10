# import flask
from flask import Flask
# create an app instance
app = Flask(__name__)


# create a route /
@app.route("/")     
# define the function my_web            
def my_web():
   # return "my_web" when
   return "Welcome to Azeez Temitope Olanrewaju webpage. I'm a DevOps Engineer with three years experience in automating CI/CD pipeline!"

# on running python app.py
if __name__ == "__main__":
   # run the flask app
   app.run()
