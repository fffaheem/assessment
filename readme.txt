This is a simple book library system implemented in Python using Flask. It allows users to add books, remove books, search for books, borrow books, and return books.


Requirements
• Python 3.x
• Flask
• POSTMAN (for testing)

to install flask : pip install flask


to run the app 
1. Clone this repository to your local machine:
	git clone https://github.com/fffaheem/assessment

2. just run the main.py file

3. Use POSTMAN or any other HTTP client to interact with the API endpoints.


* it runs in http://127.0.0.1:5000

Endpoints: 

To add a book: 
    http://127.0.0.1:5000/add_book 
    * The method is POST 
    raw JSON
    {
        "title": "Example",
        "author": "Faheem",
        "isbn": "1",
        "publication_year": 2001
    }

To delete a book: 
    http://127.0.0.1:5000/remove_book?query=2
    * The method is PUT
    provide with the ISBN number here 2 

To get all available books: 
    http://127.0.0.1:5000/all_book
    * The method is GET

To search books: 
    http://127.0.0.1:5000/search_books?query=title
    * The method is GET
    provide with anything that matches like isbn, title, author etc

To Borrow book: 
    http://127.0.0.1:5000/borrow_book?query=2
    * The method is PUT
    provide with the ISBN number here 2

To Return book: 
    http://127.0.0.1:5000/return_book?query=2
    * The method is PUT
    provide with the ISBN number here 2






