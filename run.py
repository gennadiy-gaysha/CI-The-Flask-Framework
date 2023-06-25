# Importing Flask class from flask framework
# Rendering template function from flask
import os
from flask import Flask, render_template

# Creating an instance of class Flask

# The first argument of the Flask class, is the name of the application's module - our package.
# Since we're just using a single module, we can use __name__ which is a built-in Python variable.
# Flask needs this so that it knows where to look for templates and static files.
app = Flask(__name__)

# Telling Flask what URL should trigger the function that follows


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


if __name__ == '__main__':
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', "5000")),
        debug=True)
