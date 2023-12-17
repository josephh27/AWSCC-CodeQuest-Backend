# I have read the whole README.md #
from flask import Flask
import time

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World!'


# Another example of decorators
def display_decorator(orig_func):
    def wrapper_function(*args, **kwargs):
        suffix = "with the use of display decorator."
        orig_func(*args, suffix)
    
    return wrapper_function 

@display_decorator
def display_function(*words):
    for word in words:
        print(word)

display_function('Hello', 'World', 'Goodbye')
