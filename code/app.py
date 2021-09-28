import os
import logging
from flask import Flask, render_template, abort, url_for, json, jsonify, request
app = Flask(__name__,template_folder='.')
#app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

booklist = [
    {
        "author": "hightower",
        "title": "Kubernetes up and Running"
    },
    {
        "author": "navathe",
        "title": "Database Fundamentals"
    },
    {
        "author": "ritchie",
        "title": "Let us C"
    }
]

@app.route("/")
def hello():
    return "Welcome to my bookstore!"

# read file
with open('file.json', 'r') as myfile:
    data = myfile.read()

@app.route("/welcome")
def index():
    app.logger.info('Inside Welcome')
    return render_template('index.html', title="page", jsonfile=json.dumps(data))

@app.route("/v1/books/")
def list_all_books():
    app.logger.info('Retrieving list of all books')
    list = []
    app.logger.info("list , iterating book list")
    for item in booklist:
      list.append({'book':item['title']}) 
    return jsonify(list)

@app.route("/v1/books/<string:author>")
def get_by_author(author):
    app.logger.info('Getting book by Author')
    for item in booklist:
	    if item['author'] == author:
	       data = item
    return jsonify(data)
    if not item:
        return jsonify({'error': 'Author does not exist'}), 404

@app.route("/v1/books/", methods=["POST"])
def add_book():
    author = request.json.get('author')
    book = request.json.get('title')
    if not author or not book:
        return jsonify({'error': 'Please provide Author and Title'}), 400
    else:
        data = request.get_json()
        booklist.append(data)
        return jsonify({'message': 'Added book successfully','author':author,'book': book}),200

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)
