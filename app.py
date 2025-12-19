from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Author, Book

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'

# initialize the SQLAlchemy instance defined in `models.py`
db.init_app(app)
# create a migration object to manage migrations
migrate = Migrate(app, db)

# Routes
@app.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return jsonify([author.to_dict() for author in authors])

@app.route('/authors', methods=['POST'])
def create_author():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    author = Author(name=name)
    db.session.add(author)
    db.session.commit()
    return jsonify(author.to_dict()), 201

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author_id = data.get('author_id')
    if not title or not author_id:
        return jsonify({'error': 'Title and author_id are required'}), 400
    book = Book(title=title, author_id=author_id)
    db.session.add(book)
    db.session.commit()
    return jsonify(book.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)