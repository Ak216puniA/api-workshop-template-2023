from flask import Flask, request
from db import books
from utils.auto_increment_id import increment_id
from errors import BAD_REQUEST_400, NOT_FOUND_404

app = Flask(__name__)


# Endpoint returning HTML on GET request
@app.route("/", methods=["GET"])
def webpage():
    return "<h3>This is IMG</h3>"


# Configure endpoint to return json on GET request


# CRUD operations:

# LIST:
# List all book details 
@app.route("/endpoint-url", methods=[])
def list():
    # Code
    return


# RETRIEVE:
# Retrieve book details by id
@app.route("/endpoint-url", methods=[])
def retrieve(id):  
    # Code
    return


# CREATE:
# Create new book
@app.route("/endpoint-url", methods=[])
def create():
    # Code
    return


# UPDATE:
# Update book details by id
@app.route("/endpoint-url", methods=[])
def update(id):
    # Code for complete updation through PUT request
    
    # Partial updation through PATCH request
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
        

# DELETE: 
# Delete book by id
@app.route("/endpoint-url", methods=[])
def delete(id):
    for book in books:
        if id == book["id"]:

            # Delete book from the list
            books.remove(book)

            return {}, 200

    return NOT_FOUND_404, 404
        