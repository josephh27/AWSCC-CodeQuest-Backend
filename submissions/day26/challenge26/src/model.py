from . import db

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column("id", db.Integer, primary_key=True)
    title = db.Column("title", db.String(80), unique=False, nullable=False)
    author = db.Column("author", db.String(120), unique=False, nullable=False)
    published_year = db.Column("published_year", db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}-{self.author}>'
    
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year
    
