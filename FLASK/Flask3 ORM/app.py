from flask import Flask, jsonify ,request
from flask_sqlalchemy import  SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udmw0ybt4tlrfip6qvod:iBSHgCbIOtxBAixxJoeNQAMXflngee@byncjuw7s8tagen1muul-postgresql.services.clever-cloud.com:50013/byncjuw7s8tagen1muul'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from author import Author
from members import Member
from book import Book
from genre import Genre


@app.route('/authors')
def authors():
    authors = Author.query.all()
    authors_dict = []
    for autor in authors:
       authors_dict.append(autor.dict())
    return jsonify(authors_dict)

@app.route('/authors/<int:author_id>')
def author(author_id):
    author = Author.query.get_or_404(author_id)
    return jsonify(author.dict())

@app.route('/authors/<name>')
def author_by_name(name):
    author = Author.query.filter_by(name=name).first_or_404()
    return jsonify(author.dict())

@app.route('/members',methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        registration_date=data['registration_date']
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member added successfully!'}), 201

@app.route('/members/<member_id>', methods=['GET'])
def get_member(member_id):
    member = Member.query.get_or_404(member_id)
    return jsonify({
        'member_id': member.member_id,
        'first_name': member.first_name,
        'last_name': member.last_name,
        'email': member.email,
        'registration_date': member.registration_date.isoformat()
    })
    
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    members = Member.query.all()
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    
@app.route("/books", methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = []
    for book in books:
        books_list.append({
            'book_id': book.book_id,
            'title': book.title,
            'isbn': book.isbn,
            'publication_year': book.publication_year,
            'copies': book.copies,
            'author_id': book.author_id,
            'genre_id': book.genre_id
        })
    return jsonify(books_list)

@app.route("/books/<int:book_id>", methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        'book_id': book.book_id,
        'title': book.title,
        'isbn': book.isbn,
        'publication_year': book.publication_year,
        'copies': book.copies,
        'author_id': book.author_id,
        'genre_id': book.genre_id
    })

@app.route("/books", methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        title=data['title'],
        isbn=data['isbn'],
        publication_year=data['publication_year'],
        copies=data['copies'],
        author_id=data['author_id'],
        genre_id=data['genre_id']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!'}), 201

@app.route("/books/<int:book_id>", methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    
    book.title = data.get('title', book.title)
    book.isbn = data.get('isbn', book.isbn)
    book.publication_year = data.get('publication_year', book.publication_year)
    book.copies = data.get('copies', book.copies)
    book.author_id = data.get('author_id', book.author_id)
    book.genre_id = data.get('genre_id', book.genre_id)
    
    db.session.commit()
    return jsonify({'message': 'Book updated successfully!'}), 200

@app.route("/books/<int:book_id>", methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'}), 200

if __name__ == '__main__':
    app.run() 
     