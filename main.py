from flask import Flask, request, jsonify

app = Flask(__name__)

class Book:
    def __init__(self, title, author, isbn, publication_year, status='available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.status = status

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def search_books(self, query):
        results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query.lower() in str(book.publication_year):
                results.append(book)
        return results

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == 'available':
                    book.status = 'borrowed'
                    return True
                else:
                    return False
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.status = 'available'
                return True
        return False

library = Library()

# Routes
@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    print(data)
    book = Book(data['title'], data['author'], data['isbn'], data['publication_year'])
    library.add_book(book)
    return jsonify({'message': 'Book added successfully'})

@app.route('/search_books', methods=['GET'])
def search_books():
    query = request.args.get('query')
    results = [book.__dict__ for book in library.search_books(query)]
    return jsonify(results)

@app.route('/remove_book', methods=['PUT'])
def remove_book():
    query = request.args.get('query')
    library.remove_book(query)
    return jsonify({'message': 'Book removed successfully'})

@app.route('/all_book', methods=['GET'])
def all_book():
    results = [book.__dict__ for book in library.books]
    return jsonify(results)


@app.route('/borrow_book', methods=['PUT'])
def borrow_book():
    query = request.args.get('query')
    isbn = query
    success = library.borrow_book(isbn)
    if success:
        return jsonify({'message': 'Book borrowed successfully'})
    else:
        return jsonify({'message': 'Book not available for borrowing'})

@app.route('/return_book', methods=['PUT'])
def return_book():
    query = request.args.get('query')
    isbn = query
    success = library.return_book(isbn)
    if success:
        return jsonify({'message': 'Book returned successfully'})
    else:
        return jsonify({'message': 'Book not found or already returned'})

if __name__ == '__main__':
    app.run(debug=True)