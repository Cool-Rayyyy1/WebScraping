import json
import flask
import mysql.connector
from flask import request, jsonify, Response

import sys

sys.path.insert(0, '../../')
from src.WebScraper import BookParser, AuthorParser
from src.API import queryParser

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# First connect to the sql server and get the data
conn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
c = conn.cursor(buffered=True)
c.execute('''SELECT * FROM book''')
columns = [col[0] for col in c.description]
books = [dict(zip(columns, row)) for row in c.fetchall()]
jsonBooks = json.dumps(books)

c.execute('''SELECT * FROM author''')
columns = [col[0] for col in c.description]
authors = [dict(zip(columns, row)) for row in c.fetchall()]
jsonAuthors = json.dumps(authors)
conn.commit()


# Below all the routs to various api calls
# The home page for our API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Four basic api calls</h1>
<p>A prototype API for distant reading or writing to the mysql database</p>'''


# This route will display all the books in current database
@app.route('/api/books/all', methods=['GET'])
def api_books_all():
    c.execute('''SELECT * FROM book''')
    allColumns = [col[0] for col in c.description]
    allBooks = [dict(zip(allColumns, row)) for row in c.fetchall()]
    jsonAllBooks = json.dumps(allBooks)
    return jsonAllBooks


# This route will display all the authors in current database
@app.route('/api/authors/all', methods=['GET'])
def api_authors_all():
    c.execute('''SELECT * FROM author''')
    allColumns = [col[0] for col in c.description]
    allAuthors = [dict(zip(allColumns, row)) for row in c.fetchall()]
    jsonAllAuthors = json.dumps(allAuthors)
    return jsonAllAuthors


# This route will search one author in the database based on the authorId
@app.route('/api/author', methods=['GET'])
def api_get_authorID():
    inputId = request.args.get('id')
    if inputId is None:
        return "Error: No id field provided. Please specify an id."
    results = []
    for author in authors:
        if author["author_Id"] == inputId:
            results.append(author)
    if len(results) == 0:
        return "Error: Can not find corresponding author！"
    else:
        return jsonify(results)


# This route will search one book in the database based on the bookId
@app.route('/api/book', methods=['GET'])
def api_get_bookID():
    inputId = request.args.get('id')
    if inputId is None:
        return "Error: No id field provided. Please specify an id."
    results = []
    for book in books:
        if book["book_id"] == inputId:
            results.append(book)
    if len(results) == 0:
        return "Error: Can not find corresponding book！"
    else:
        return jsonify(results)


# This route will search the book or author based the complex query
@app.route('/api/search', methods=['GET'])
def api_query_search():
    try:
        query = request.args.get('q')
        parser = queryParser.Query(query)
        result = parser.startParsing()
        if not isinstance(result, list):
            return result
        else:
            return jsonify(result)

    except Exception as e:
        return str(e)

# A helper function for the top k api
def takeSecond(elem):
    return elem[1]

# This route will search the top k rating book
@app.route('/api/top/book', methods=['GET'])
def api_top_bookId():
    inputK = request.args.get('t')
    if inputK is None:
        return "Error: No top number provided. Please specify an number."
    try:
        sql = "SELECT book_id, rating FROM Book"
        c.execute(sql)
        conn.commit()
        tempList = c.fetchall()
        nonSortList = []
        for data in tempList:
            nonSortList.append((data[0], float(data[1])))
        sortList = sorted(nonSortList, key=takeSecond, reverse=True)
        finalList = []
        for i in range(int(inputK)):
            finalList.append(sortList[i])
        returnList = []
        for each in finalList:
            searchSql = "SELECT * FROM Book WHERE book_id = %s"
            target = (each[0],)
            c.execute(searchSql, target)
            searchResult = c.fetchall()
            returnList.append(searchResult)
        return jsonify(returnList)

    except Exception as e:
        return e

# This route will search the top k rating author
@app.route('/api/top/author', methods=['GET'])
def api_top_authorId():
    inputK = request.args.get('t')
    if inputK is None:
        return "Error: No top number provided. Please specify an number."
    try:
        sql = "SELECT author_Id, rating FROM Author"
        c.execute(sql)
        conn.commit()
        tempList = c.fetchall()
        nonSortList = []
        for data in tempList:
            nonSortList.append((data[0], float(data[1])))
        sortList = sorted(nonSortList, key=takeSecond, reverse=True)
        finalList = []
        for i in range(int(inputK)):
            finalList.append(sortList[i])
        returnList = []
        for each in finalList:
            searchSql = "SELECT * FROM Author WHERE author_Id = %s"
            target = (each[0],)
            c.execute(searchSql, target)
            searchResult = c.fetchall()
            returnList.append(searchResult)
        return jsonify(returnList)

    except Exception as e:
        return e

# This route will change the information of the book based on the given bookId. You need to pass in a json in the postman.
@app.route('/api/book', methods=['PUT'])
def api_put_books():
    inputId = request.args.get('id')
    if inputId is None:
        return "Error: No id field provided. Please specify an id."
    try:
        sql = "SELECT book_id, COUNT(*) FROM Book WHERE book_id = %s GROUP BY book_id"
        target = (inputId,)
        c.execute(sql, target)
        row_count = c.rowcount
        if row_count == 0:
            return Response(response=json.dumps(dict(error="No such book id is found")), status=400)
        try:
            inputData = request.form.to_dict()
            key = list(inputData.keys())[0]
            value = str(inputData[key])

        except:
            return Response(response=json.dumps(dict(error="unsupported data type")), status=415)

        if key == "ISBN":
            sql = "UPDATE Book SET ISBN = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "book_url":
            sql = "UPDATE Book SET book_url = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "title":
            sql = "UPDATE Book SET title = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "author_url":
            sql = "UPDATE Book SET author_url = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "author":
            sql = "UPDATE Book SET author = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "rating":
            sql = "UPDATE Book SET rating = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "rating_count":
            sql = "UPDATE Book SET rating_count = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "review_count":
            sql = "UPDATE Book SET review_count = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "image_url":
            sql = "UPDATE Book SET image_url = %s WHERE book_id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)

    except Exception as e:
        return str(e)


# This route will change the information of the author based on the given authorId. You need to pass in a json by postman.
@app.route('/api/author', methods=['PUT'])
def api_put_authors():
    inputId = request.args.get('id')
    if inputId is None:
        return "Error: No id field provided. Please specify an id."
    try:
        sql = "SELECT author_Id, COUNT(*) FROM Author WHERE author_Id = %s GROUP BY author_Id"
        target = (inputId,)
        c.execute(sql, target)
        row_count = c.rowcount
        if row_count == 0:
            return Response(response=json.dumps(dict(error="No such author id is found")), status=400)
        try:
            inputData = request.form.to_dict()
            key = list(inputData.keys())[0]
            value = str(inputData[key])

        except:
            return Response(response=json.dumps(dict(error="unsupported data type")), status=415)

        if key == "name":
            sql = "UPDATE Author SET name = %s WHERE author_Id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "author_url":
            sql = "UPDATE Author SET author_url = %s WHERE author_Id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "rating":
            sql = "UPDATE Author SET rating = %s WHERE author_Id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "rating_count":
            sql = "UPDATE Author SET rating_count = %s WHERE author_Id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "review_count":
            sql = "UPDATE Author SET review_count = %s WHERE author_Id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)
        elif key == "image_url":
            sql = "UPDATE Author SET image_url = %s WHERE author_Id = %s"
            update = (value, inputId)
            c.execute(sql, update)
            conn.commit()
            return Response(response=json.dumps(dict(message="updated")), status=200)

    except Exception as e:
        return str(e)


# This route will add a new book in our database. You need to pass in a json format dic in postman.
@app.route('/api/book', methods=['POST'])
def api_post_book():
    try:
        inputData = request.json
        if isinstance(inputData, list):
            return Response(response=json.dumps(dict(error="a single book is required")), status=415)
        book_id = inputData["book_id"]
        book_url = inputData["book_url"]
        book_title = inputData["title"]
        book_ISBN = inputData["ISBN"]
        book_authorUrl = inputData["author_url"]
        book_author = inputData["author"]
        book_rating = inputData["rating"]
        book_ratingCount = inputData["rating_count"]
        book_reviewCount = inputData["review_count"]
        book_imageUrl = inputData["image_url"]
        book_similar = json.dumps(inputData["similar_books"])
        c.execute('''INSERT INTO Book VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
            book_id, book_url, book_title, book_ISBN, book_authorUrl, book_author, book_rating, book_ratingCount,
            book_reviewCount,
            book_imageUrl, book_similar))
        conn.commit()
        return Response(response=json.dumps(dict(message="added")), status=200)

    except Exception as e:
        return str(e)


# This route will add a list of books in our database. You need to pass in a json format list books in postman
@app.route('/api/books', methods=['POST'])
def api_post_books():
    try:
        inputData = request.json
        if not isinstance(inputData, list):
            return Response(response=json.dumps(dict(error="multiple books are required")), status=415)
        for data in inputData:
            book_id = data["book_id"]
            book_url = data["book_url"]
            book_title = data["title"]
            book_ISBN = data["ISBN"]
            book_authorUrl = data["author_url"]
            book_author = data["author"]
            book_rating = data["rating"]
            book_ratingCount = data["rating_count"]
            book_reviewCount = data["review_count"]
            book_imageUrl = data["image_url"]
            book_similar = json.dumps(data["similar_books"])
            c.execute('''INSERT INTO Book VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                book_id, book_url, book_title, book_ISBN, book_authorUrl, book_author, book_rating, book_ratingCount,
                book_reviewCount, book_imageUrl, book_similar))
            conn.commit()
        return Response(response=json.dumps(dict(message="added")), status=200)

    except Exception as e:
        return str(e)


# This route will add a author in our database. You need to pass in a json format dic in postman
@app.route('/api/author', methods=['POST'])
def post_author():
    try:
        inputData = request.json
        if isinstance(inputData, list):
            return Response(response=json.dumps(dict(error="a single author is required")), status=415)
        author_id = inputData["author_Id"]
        author_name = inputData["name"]
        author_url = inputData["author_url"]
        author_rating = inputData["rating"]
        author_ratingCount = inputData["rating_count"]
        author_reviewCount = inputData["review_count"]
        author_image_url = inputData["image_url"]
        author_related_authors = json.dumps(inputData["related_author"])
        author_books = json.dumps(inputData["author_books"])
        c.execute('''INSERT INTO Author VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
            author_id, author_name, author_url, author_rating, author_ratingCount, author_reviewCount, author_image_url,
            author_related_authors, author_books))
        conn.commit()
        return Response(response=json.dumps(dict(message="added")), status=200)
    except Exception as e:
        return str(e)


# This route will add a list of authors in our database. You need to pass in a json format list in postman
@app.route('/api/authors', methods=['POST'])
def post_authors():
    try:
        inputData = request.json
        if not isinstance(inputData, list):
            return Response(response=json.dumps(dict(error="multiple authors are required")), status=415)
        for data in inputData:
            author_id = data["author_Id"]
            author_name = data["name"]
            author_url = data["author_url"]
            author_rating = data["rating"]
            author_ratingCount = data["rating_count"]
            author_reviewCount = data["review_count"]
            author_image_url = data["image_url"]
            author_related_authors = json.dumps(data["related_author"])
            author_books = json.dumps(data["author_books"])
            c.execute('''INSERT INTO Author VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                author_id, author_name, author_url, author_rating, author_ratingCount, author_reviewCount,
                author_image_url, author_related_authors, author_books))
            conn.commit()
        return Response(response=json.dumps(dict(message="added")), status=200)

    except Exception as e:
        return str(e)


# This route will scrape a url information and store the information in the database. You need you pass in a url after the route.
@app.route('/api/scrape', methods=['POST'])
def post_scrape():
    try:
        input_url = request.args.get('url')
        if input_url is None:
            return Response(response=json.dumps(dict(error="invalid parameter")), status=400)
        else:
            currentBook = BookParser.Book(input_url)
            currentAuthor = AuthorParser.Author(currentBook.getAuthorUrl())

            # store book information
            bookUrl = currentBook.getBookUrl()
            bookName = currentBook.getTitle()
            print("start scraping " + bookName + " !")
            bookId = currentBook.getBookId()
            bookISBN = currentBook.getISBN()
            authorUrl = currentBook.getAuthorUrl()
            authorName = currentBook.getAuthor()
            bookRating = currentBook.getRating()
            bookRatingCount = currentBook.getRatingCount()
            bookReviewCount = currentBook.getReviewCount()
            bookImageUrl = currentBook.getBookImageUrl()
            similarBook, similarUrl = currentBook.getSimilarBooks()
            jsonOfSimilar = json.dumps(similarBook)
            c.execute('''INSERT INTO Book VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                bookId, bookUrl, bookName, bookISBN, authorUrl, authorName, bookRating, bookRatingCount,
                bookReviewCount,
                bookImageUrl, jsonOfSimilar))
            conn.commit()
            # store author information
            authorName = currentAuthor.getName()
            print("start scraping " + authorName + " !")
            authorId = currentAuthor.getAuthorId()
            authorRating = currentAuthor.getRating()
            authorRatingCount = currentAuthor.getRatingCount()
            authorReviewCount = currentAuthor.getReviewCount()
            authorImageUrl = currentAuthor.getImageUrl()
            listOfRelated = currentAuthor.getRelatedAuthors()
            jsonOfRelated = json.dumps(listOfRelated)
            listOfAuthorBooks = currentAuthor.getAuthorsBooks()
            jsonOfAuthorBooks = json.dumps(listOfAuthorBooks)
            c.execute('''INSERT INTO Author VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                authorId, authorName, authorUrl, authorRating, authorRatingCount, authorReviewCount, authorImageUrl,
                jsonOfRelated, jsonOfAuthorBooks))
            conn.commit()

            return Response(response=json.dumps(dict(message="success")), status=200)
    except Exception as e:
        return str(e)


# This route will delete a single book
@app.route('/api/book', methods=['DELETE'])
def delete_book():
    inputId = request.args.get('id')
    if inputId is None:
        return "Error: No id field provided. Please specify an id."
    try:
        sql = "SELECT book_id, COUNT(*) FROM Book WHERE book_id = %s GROUP BY book_id"
        target = (inputId,)
        c.execute(sql, target)
        row_count = c.rowcount
        if row_count == 0:
            return Response(response=json.dumps(dict(message="No such book id is found therefore no deletion")),
                            status=400)
        else:
            deleteSQL = "DELETE FROM Book WHERE book_id = %s"
            c.execute(deleteSQL, target)
            conn.commit()
            return Response(response=json.dumps(dict(message="deleted")), status=200)
    except Exception as e:
        return str(e)


# This method will delete a single author
@app.route('/api/author', methods=['DELETE'])
def delete_author():
    inputId = request.args.get('id')
    if inputId is None:
        return "Error: No id field provided. Please specify an id."
    try:
        sql = "SELECT author_Id, COUNT(*) FROM Author WHERE author_Id = %s GROUP BY author_Id"
        target = (inputId,)
        c.execute(sql, target)
        row_count = c.rowcount
        if row_count == 0:
            return Response(response=json.dumps(dict(message="No such author id is found therefore no deletion")),
                            status=400)
        else:
            deleteSQL = "DELETE FROM Author WHERE author_Id = %s"
            c.execute(deleteSQL, target)
            conn.commit()
            return Response(response=json.dumps(dict(message="deleted")), status=200)
    except Exception as e:
        return str(e)


app.run()
