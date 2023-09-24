from flask import Flask,jsonify,request

app=Flask(__name__)

books=[
    {"id":1,"title":"Book1","author":"Manohar 1"},
    {"id":2,"title":"Book2","author":"Manohar 2"},
    {"id":3,"title":"Book3","author":"Manohar 3"},
    {"id":4,"title":"Book4","author":"Manohar 4"},
    {"id":5,"title":"Book5","author":"Manohar 5"},
    {"id":6,"title":"Book6","author":"Manohar 6"},
]
@app.route('/',methods=['GET'])
def home_page():
    return 'Home Page'

#route to get all books
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

#route to get specific book by ID
@app.route('/books/<int:book_id>',methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id']==book_id:
            return jsonify(book)
    return jsonify({'error':'Book not Found'})


#route to add new book
@app.route('/books',methods=['POST'])
def add_book():
    new_book={
        "id":request.json['id'],
        "title":request.json['title'],
        "author":request.json['author'],
    }
    books.append(new_book)
    return jsonify({'message':'Book added successfully'})


#route to update an existing book
@app.route('/books/<int:book_id>',methods=['PUT'])
def update_book(book_id):
    for book in books:
        if book['id']==book_id:
            book['title']=request.json['title']
            book['author']=request.json['author']
            return jsonify({'message':'Book Updated Successfuly'})
    return jsonify({'error':'Book not Found'})



#route to delete an existing book
@app.route('/books/<int:book_id>',methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id']==book_id:
            books.remove(book)
            return jsonify({'message':'Book deleted Successfuly'})
    return jsonify({'error':'Book not Found'})




if __name__=='__main__':
    app.run(debug=True)