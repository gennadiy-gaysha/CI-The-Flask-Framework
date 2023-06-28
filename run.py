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

# 'request' library from Flask.
# Request is going to handle things like finding out what method
# we used, and it will also contain our form object when we've posted it.

# Sometimes we want to display a non-permanent message to the user,
# something that only stays on screen until we refresh the page, or
# go to a different one. These are called 'flashed messages' in Flask.
from flask import Flask, render_template, request, flash

# We want Python to import the data. To do that, we first need
# to import the JSON library, because we're going to be passing
# the data that's coming in as JSON.
import json

if os.path.exists('env.py'):
      import env


# Creating an instance of class Flask

# The first argument of the Flask class, is the name of the
# application's module - our package. Since we're just using
# a single module, we can use __name__ which is a built-in
# Python variable. Flask needs this so that it knows where
# to look for templates and static files.
app = Flask(__name__)
# This line assigns a secret key to the Flask application.
app.secret_key = os.environ.get('SECRET_KEY')

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
   #  initializing empty list
    data = []
   #  We need to have Python open the JSON file in order to read it.
   #  This is called a 'with' block.
   # Python is opening the JSON file as "read-only", and assigning the contents
   # of the file to a new variable we've created called json_data.
    with open("data/company.json", "r") as json_data:
       data = json.load(json_data)
   #  This is assigning a new variable called 'company'
   #  that will be sent through to the HTML template, which is
   #  equal to the list of data it's loading from the JSON file.
    return render_template('about.html', page_title="About", company=data)

@app.route("/about/<member_name>")
def about_member(member_name):
        member = {}
        with open("data/company.json", 'r') as json_data:
                data = json.load(json_data)
                for obj in data:
                        if obj["url"] == member_name:
                                        member = obj
# This first 'member' is the variable name being passed through into our html file.
# The second 'member' is the member object we created above on line 76.
        return render_template('member.html', member=member)


@app.route('/contacts', methods = ["GET", "POST"])
def contacts():
    if request.method == 'POST':
         #  print(request.form.get("name"))
         #  print(request.form['email'])
         flash("Thanks {}, we have received your message!".format(
               request.form.get("name")))
    return render_template('contacts.html', page_title="Contacts")


@app.route('/careers')
def careers():
    return render_template('/careers.html', page_title="Careers")


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
