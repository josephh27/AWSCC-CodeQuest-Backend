from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "new_books.db"
db =  SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    from .model import Book

    with app.app_context():
        db.create_all()

    from .views import views, faculty_views
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(faculty_views, url_prefix="/faculty")

    return app