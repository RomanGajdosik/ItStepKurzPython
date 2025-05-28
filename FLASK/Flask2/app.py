from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)


@app.route('/')
def home():
    return 'Nasa kniznica'


@app.route('/knihy', methods=['GET'])
def get_books():
    return jsonify({'books': books})


@app.route('/knihy', methods=['POST'])
def add_book():
    print(request)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/knihy/<int:id>",methods=["GET"])
def find_book(id):

    for book in books :
        if  book['id'] == id:
            return jsonify({'Book':book})
    abort(404)  # Vráti HTTP 404 Not Found


@app.route('/knihy/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book['id'] == id:
            if not request.json or 'title' not in request.json or 'author' not in request.json:
                abort(400)  # HTTP 400 Bad Request

            book['title'] = request.json['title']
            book['author'] = request.json['author']
            return jsonify(book)

    abort(404)  # HTTP 404 Not Found

@app.route('/knihy/<int:id>',methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.pop(id-1)
            return f"Kniha odstranena uspesne"
    abort(404)

@app.route('/knihy/filter', methods=['GET'])
def filter_books():
    title = request.args.get('title')
    author = request.args.get('author')

    filtered_books = [
        book for book in books
        if (not title or title.lower() in book['title'].lower()) and
           (not author or author.lower() in book['author'].lower())
    ]

    return jsonify({'books': filtered_books})


@app.route('/knihy/sort', methods=['GET'])
def sort_books():
    by = request.args.get('by', 'id')  # Defaultne zoradenie podľa ID
    order = request.args.get('order', 'ASC').upper()  # Defaultne vzostupné zoradenie

    if by not in ['id', 'title', 'author']:
        abort(400, description="Neplatná hodnota pre 'by'. Použite 'id', 'title' alebo 'author'.")

    reverse = (order == 'DESC')

    sorted_books = sorted(books, key=lambda x: x[by], reverse=reverse)

    return jsonify({'sorted_books': sorted_books})


if __name__ == '__main__':
    app.run()