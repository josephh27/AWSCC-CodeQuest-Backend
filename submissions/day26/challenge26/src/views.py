from flask import Blueprint, render_template
from . import db
from .model import Book

views = Blueprint("views", __name__)

@views.route("/")
def home():
    new_book = Book(title="JJK", author="Harper", published_year=1960)
    db.session.add(new_book)
    db.session.commit()
    books = Book.query.all()
    return render_template("home.html", books=books)