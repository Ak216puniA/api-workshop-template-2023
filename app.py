from flask import Flask, jsonify, request
from db import books
from utils.auto_increment_id import increment_id
from errors import BAD_REQUEST_400, NOT_FOUND_404

app = Flask(__name__)


# returning HTML for GET request at this endpoint
@app.route("/", methods=["GET"])
def webpage():
    return "<h3>This is IMG</h3>"


# returning JSON for GET request at this endpoint
@app.route("/img/")
def home():
    return {"data": "IMG"}, 200


# Retrieve book details by id
@app.route("/books/<int:id>/", methods=["GET"])
def retrieve(id):  
    # Time complexity O(N)
    for book in books:
        if id == book["id"]:
            return book, 200

    return NOT_FOUND_404, 404


# List all book details 
@app.route("/books/", methods=["GET"])
def list():
    return books, 200


# Create new book
@app.route("/books/", methods=["POST"])
def create():
    try:
        title = request.json["title"]
        author = request.json["author"]
        # Validate data
    except KeyError:
        return BAD_REQUEST_400, 400
    
    id_to_be_assigned = increment_id()

    book_created = {
        "id": id_to_be_assigned,
        "title": title,
        "author": author
    }

    # Constant time complexity. So, relax!!
    books.append(book_created)
    return book_created, 201
    

# Update book details by id
@app.route("/books/<int:id>/", methods=["PUT", "PATCH"])
def update(id):
    # Complete updation
    if request.method == "PUT":

        for book in books:
            if id == book["id"]:
                try:
                    title = request.json["title"]
                    author = request.json["author"]
                except KeyError:
                    return BAD_REQUEST_400, 400
                
                # Update book details
                book["title"] = title
                book["author"] = author

                return book, 200
            
        return NOT_FOUND_404, 404
    
    # Partial updation
    if request.method == "PATCH":

        for book in books:
            if id == book["id"]:
                
                title = book["title"]
                author = book["author"]

                # New title
                if "title" in request.json:
                    title = request.json["title"]
                # New author
                if "author" in request.json:
                    author = request.json["author"]

                # Update book details
                book["title"] = title
                book["author"] = author

                return book, 200
            
        return NOT_FOUND_404, 404
        

# Delete book by id
@app.route("/books/<int:id>/", methods=["DELETE"])
def delete(id):
    for book in books:
        if id == book["id"]:

            # Delete book from the list
            books.remove(book)

            return {}, 200

    return NOT_FOUND_404, 404
        