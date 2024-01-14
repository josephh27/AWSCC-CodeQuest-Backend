from flask import Blueprint, render_template, jsonify
from . import db
from .model import Book

# This is just a group of routes
views = Blueprint("views", __name__)

@views.route("/")
def home():
    new_book = Book(title="JJK", author="Harper", published_year=1960)
    db.session.add(new_book)
    db.session.commit()
    books = Book.query.all()
    return render_template("home.html", books=books)

@views.route("/about")
def about():
    return jsonify({
        "name": "Books",
        "Website-Type": "Static"
    })

faculty_views = Blueprint("faculty_views", __name__)

@faculty_views.route("/")
def home():
    new_book = Book(title="How to Teach", author="Harper", published_year=1960)
    db.session.add(new_book)
    db.session.commit()
    books = Book.query.all()
    return render_template("home.html", books=books)

@faculty_views.route("/about")
def about():
    return jsonify({
        "name": "Faculty",
        "Website-Type": "Static"
    })
