""" Adopt A PET Project - Lesson 23 - Assignment01 """

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension



app = Flask(__name__)  # creating an instance of the Flask Class

app.config['SECRET_KEY'] = "RalphsCode-123"
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('home.html')