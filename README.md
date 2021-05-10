Creating a basic Flask Application

To create a Flask application we need to install the Flask package for python. But before we do that it is advisable to always create a virtual environment so that everything we will do doesn’t affect the Python installed on our machine.

Step 1: Installations
Create the application directory:
mkdir my_flask_app
cd my_flask_app

Install python virtual environment with pip: 
pip install virtualenv

Create a virtual environment for our app:
virtualenv venv

Activate the virtual environment we created:
source venv/bin/activate

Install the Flask package:
pip install Flask

Save all the packages in a file:
pip freeze > requirements.txt

Step 2: Build the Flask Application
The first step in creating our flask application is to create a file and name it app.py. Then open the file with your preferred IDE or editor to start coding.

To run the app on your local machine do:
python app.py

Step 3: Serve HTML/Template Files
Flask allows us to display contents to our users with HTML.

Flask reads HTML files from a directory called templates and reads assets like your CSS, Javascript and images from the static directory.
Create templates and static directories inside our my_flask_app directory:
mkdir templates static

Create a new file in the templates directory and name it home.html.

Create a route and function to serve our HTML file. To serve HTML files in flask, we will import and use a Flask function called render_template.

Run the application on your local machine by running:
Navigate to localhost:5000/home on your preferred browser to view your Flask application.
