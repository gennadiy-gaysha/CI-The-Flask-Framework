# Goal: run a server-side poroject.
# 1) We will serve HTML files from our server.
# 2) We'll use the Jinja templating language to write logic
# inside of our HTML templates, which allows us to use
# Python for-loops, if-statements, and also inheritance.
# 3) We'll also learn how to submit forms, which will allow us
# to take data from the client and display it on the server.

# 1) Create and running a Flask application.
# 2) Serve HTML, CSS, and JavaScript files from the backend.
# 3) Make our code reusable by using template logic.
# 4) Post data from HTML forms.
# 5) Deploy our project using a platform called Heroku so that
# it's served externally for all the world to see.

# Importing Flask class from flask framework
# Rendering template function from flask
import os
# We import the render_template() function from Flask.
# Then, instead of returning text, We are going to return
# render_template("index.html").
# Where does Flask find this index.html file?
# Flask expects it to be a directory called templates, which
# should be at the same level as our run.py file.
from flask import Flask, render_template

# Creating an instance of class Flask

# The first argument of the Flask class, is the name of the
# application's module - our package. Since we're just using
# a single module, we can use __name__ which is a built-in
# Python variable. Flask needs this so that it knows where
# to look for templates and static files.
app = Flask(__name__)

# Decorator (uses pai-notation - @) - is the way of wrapping
# functions.
# When the user tries to browse to the root directory, Flask thiggers
# the index function
# Tells Flask what URL should trigger the function that follows

# ROUTING: when we go to the "/" on the top-level of our domain,
# it then returns the template from our index() function.
# The root decorator binds the index() function to itself, so that
# whenever that root is called, the function is called.
# This function is also called a 'view'.


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/career')
def career():
    return render_template('/career.html')


# The word 'main' wrapped in double-underscores (__main__) is the name of the default
# module in Python. This is the first one that we run, so if this has not been imported,
# which it won't be, then it's going to be run directly.
if __name__ == '__main__':
    # if True, then we are going to run our application with a set
    #  of arguments
    app.run(
        # The 'host' will be set to os.environ.get("IP"),
        # We set a default of "0.0.0.0".
        # We're using the os module from the standard library to get the 'IP'
        # environment variable if it exists, but set a default value if it's not found.
        host=os.environ.get('IP', '0.0.0.0'),
        # The same with 'PORT', but this time, we're casting it as an integer, and we
        # will set that default to "5000", which is a common port used by Flask.
        port=int(os.environ.get('PORT', "5000")),
        # We also need to specify "debug=True", because that will allow us to debug our
        # code much easier during the development stage. Also we should never have
        # "debug=True" in a production application, or when we submit our projects for
        # assessment.This is very important, because having debug=True can allow arbitrary
        # code to be run, and obviously this is a security flaw.
        debug=True)
