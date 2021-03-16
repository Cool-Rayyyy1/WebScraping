import mysql.connector
from src.API import queryParser
import sys

sys.path.insert(0, '../../')
from src.WebScraper import BookParser, AuthorParser
import json


# This file contains the function to achieve the Command Line Application

# Helper function to check if the url points to a book goodReader website
def checkGoodReaderUrl(url):
    if "goodreads.com/book/show/" in url:
        return True
    else:
        return False


# Helper function to handle get the information of a book or author
def getDistribution(target, id):
    if target == "Book":
        sql = "SELECT * From Book WHERE book_id = %s"
        objectId = (id,)
        c.execute(sql, objectId)
        getResult = c.fetchall()
        conn.commit()
        return getResult
    else:
        sql = "SELECT * From Author WHERE author_Id = %s"
        objectId = (id,)
        c.execute(sql, objectId)
        getResult = c.fetchall()
        conn.commit()
        return getResult


# Helper function to scrape the information of a website
def scraping(currentUrl):
    currentBook = BookParser.Book(currentUrl)
    currentAuthor = AuthorParser.Author(currentBook.getAuthorUrl())

    ## store book information
    bookUrl = currentBook.getBookUrl()
    bookName = currentBook.getTitle()
    print("start scraping " + bookName + " !")

    bookId = currentBook.getBookId().replace(' ', '')
    bookISBN = currentBook.getISBN().replace(' ', '')
    authorUrl = currentBook.getAuthorUrl()
    authorName = currentBook.getAuthor()
    bookRating = currentBook.getRating().replace(' ', '')
    bookRating = bookRating.replace("\n", '')
    bookRatingCount = currentBook.getRatingCount().replace(' ', '')
    bookRatingCount = bookRatingCount.replace("\n", '')
    bookReviewCount = currentBook.getReviewCount().replace(' ', '')
    bookReviewCount = bookReviewCount.replace("\n", '')
    bookImageUrl = currentBook.getBookImageUrl()
    similarBook, similarUrl = currentBook.getSimilarBooks()
    jsonOfSimilar = json.dumps(similarBook)
    c.execute('''INSERT INTO Book VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
        bookId, bookUrl, bookName, bookISBN, authorUrl, authorName, bookRating, bookRatingCount, bookReviewCount,
        bookImageUrl, jsonOfSimilar))

    ## store author information

    authorName = currentAuthor.getName()
    print("start scraping " + authorName + " !")
    authorId = currentAuthor.getAuthorId().replace(' ', '')
    authorRating = currentAuthor.getRating().replace(' ', '')
    authorRating = authorRating.replace("\n", '')
    authorRatingCount = currentAuthor.getRatingCount().replace(' ', '')
    authorRatingCount = authorRatingCount.replace("\n", '')
    authorReviewCount = currentAuthor.getReviewCount().replace(' ', '')
    authorReviewCount = authorReviewCount.replace("\n", '')
    authorImageUrl = currentAuthor.getImageUrl()
    listOfRelated = currentAuthor.getRelatedAuthors()
    jsonOfRelated = json.dumps(listOfRelated)
    listOfAuthorBooks = currentAuthor.getAuthorsBooks()
    jsonOfAuthorBooks = json.dumps(listOfAuthorBooks)
    c.execute('''INSERT INTO Author VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
        authorId, authorName, authorUrl, authorRating, authorRatingCount, authorReviewCount, authorImageUrl,
        jsonOfRelated, jsonOfAuthorBooks))
    conn.commit()

    print("scraping done!")


# Helper function to delete data in our database
def deleteHelper(target, id):
    if target == "Book":
        sql = "DELETE FROM Book WHERE book_id = %s"
        objectId = (id,)
        c.execute(sql, objectId)
        conn.commit()
    else:
        sql = "DELETE From Author WHERE author_Id = %s"
        objectId = (id,)
        c.execute(sql, objectId)
        conn.commit()
    print("successfully delete !")


# Main method to start our command line application
if __name__ == '__main__':
    # connect to sql server
    conn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
    c = conn.cursor(buffered=True)
    result = 0
    while 1 > 0:
        print("Please enter which function you want to use")
        startCommand = input('>')
        if startCommand == "GET":
            result = 1
            break
        elif startCommand == "SEARCH":
            result = 2
            break
        elif startCommand == "UPDATE":
            result = 3
            break
        elif startCommand == "CREATE":
            result = 4
            break
        elif startCommand == "SCRAPE":
            result = 5
            break
        elif startCommand == "DELETE":
            result = 6
            break
        else:
            print("please enter valid startCommand!")

    #Start to handle different situations
    # Get
    if result == 1:
        while 1 > 0:
            print("Which object you want to get? Author or Book")
            command = input('>')
            if command == "Author":
                target = "Author"
                break
            elif command == "Book":
                target = "Book"
                break
            else:
                print("please enter valid object")
        while 1 > 0:
            print("Enter object id?")
            command = input('>')
            if len(command) != 0:
                id = int(command)
                break
            else:
                print("please enter valid id")

        getResult = getDistribution(target, id)
        if len(getResult) == 0:
            print("No such item exist!")
        else:
            print(getResult)

    # SEARCH
    elif result == 2:
        while 1 > 0:
            print("Please enter query!")
            command = input('>')
            if len(command) != 0:
                query = command
                break
            else:
                print("please enter valid query")
        parser = queryParser.Query(query)
        parseResult = parser.startParsing()
        print(parseResult)

    # UPDATE
    elif result == 3:
        while 1 > 0:
            print("Which object you want to update? Author or Book")
            command = input('>')
            if command == "Author":
                target = "Author"
                break
            elif command == "Book":
                target = "Book"
                break
            else:
                print("please enter valid object")
        while 1 > 0:
            print("Enter object id?")
            command = input('>')
            if len(command) != 0:
                id = int(command)
                break
            else:
                print("please enter valid id")

        getResult = getDistribution(target, id)
        if len(getResult) == 0:
            print("No such item exist!")
        else:
            print("This is the Object that you want tp update!")
            print(getResult)
        while 1 > 0:
            print("Enter the filed that you want to update!")
            field = input('>')
            if len(field) != 0:
                break
            else:
                print("please enter valid field")
        while 1 > 0:
            print("Enter value you want to update!")
            update = input('>')
            if len(update) != 0:
                break
            else:
                print("please enter valid field")
        if target == "Book":
            if field == "book_id":
                sql = "UPDATE Book SET book_id = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "book_url":
                sql = "UPDATE Book SET book_url = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "title":
                sql = "UPDATE Book SET title = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "ISBN":
                sql = "UPDATE Book SET ISBN = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "author_url":
                sql = "UPDATE Book SET author_url; = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "author":
                sql = "UPDATE Book SET author = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "rating":
                sql = "UPDATE Book SET rating = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "rating_count":
                sql = "UPDATE Book SET rating_count = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "review_count":
                sql = "UPDATE Book SET review_count = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "image_url":
                sql = "UPDATE Book SET image_url = %s WHERE book_id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
        else:
            if field == "author_Id":
                sql = "UPDATE Author SET author_Id = %s WHERE author_Id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "name":
                sql = "UPDATE Author SET name = %s WHERE author_Id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "author_url":
                sql = "UPDATE Author SET author_url = %s WHERE author_Id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "rating":
                sql = "UPDATE Author SET rating = %s WHERE author_Id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "rating_count":
                sql = "UPDATE Author SET rating_count = %s WHERE author_Id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "review_count":
                sql = "UPDATE Author SET review_count = %s WHERE author_Id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
            elif field == "image_url":
                sql = "UPDATE Author SET image_url = %s WHERE author_Id = %s"
                newVal = (update, id)
                c.execute(sql, newVal)
                conn.commit()
        print("Successfully update!")
        newResult = getDistribution(target, id)
        print(newResult)

    # CREATE
    elif result == 4:
        while 1 > 0:
            print("Which object you want to create? Author or Book")
            command = input('>')
            if command == "Author":
                createTarget = "Author"
                break
            elif command == "Book":
                createTarget = "Book"
                break
            else:
                print("please enter valid object")
        if createTarget == "Book":
            while 1 > 0:
                print("Enter book_id!")
                book_id = input('>')
                if len(book_id) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter book_url!")
                book_url = input('>')
                if len(book_url) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter title!")
                book_title = input('>')
                if len(book_title) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter ISBN")
                book_ISBN = input('>')
                if len(book_ISBN) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_url!")
                book_authorUrl = input('>')
                if len(book_authorUrl) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author name!")
                book_author = input('>')
                if len(book_author) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter book_rating!")
                book_rating = input('>')
                if len(book_rating) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter book_ratingCount!")
                book_ratingCount = input('>')
                if len(book_ratingCount) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter book_reviewCount")
                book_reviewCount = input('>')
                if len(book_reviewCount) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter book_imageUrl!")
                book_imageUrl = input('>')
                if len(book_imageUrl) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter similar Books!")
                book_similarBooks = input('>')
                if len(book_similarBooks) != 0:
                    book_similarJson = json.dumps(book_similarBooks)
                    break
                else:
                    print("Please enter valid value!")
            c.execute('''INSERT INTO Book VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                book_id, book_url, book_title, book_ISBN, book_authorUrl, book_author, book_rating, book_ratingCount,
                book_reviewCount,
                book_imageUrl, book_similarJson))
            conn.commit()
            print("successful create!")
        else:
            while 1 > 0:
                print("Enter author_id!")
                author_id = input('>')
                if len(author_id) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_name!")
                author_name = input('>')
                if len(author_name) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_url!")
                author_url = input('>')
                if len(author_url) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_rating!")
                author_rating = input('>')
                if len(author_rating) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_ratingCount!")
                author_ratingCount = input('>')
                if len(author_ratingCount) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_reviewCount!")
                author_reviewCount = input('>')
                if len(author_reviewCount) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_ImageUrl!")
                author_ImageUrl = input('>')
                if len(author_ImageUrl) != 0:
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_related!")
                author_related = input('>')
                if len(author_related) != 0:
                    author_relatedJson = json.dumps(author_related)
                    break
                else:
                    print("Please enter valid value!")
            while 1 > 0:
                print("Enter author_books!")
                author_books = input('>')
                if len(author_books) != 0:
                    break
                else:
                    print("Please enter valid value!")
            c.execute('''INSERT INTO Author VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                author_id, author_name, author_url, author_rating, author_ratingCount, author_reviewCount,
                author_ImageUrl,
                author_relatedJson, author_books))
            conn.commit()
            print("successful create!")

    # SCRAPE
    elif result == 5:
        while 1 > 0:
            print("Please enter a valid GoodReader address!")
            startUrl = input('>')
            if checkGoodReaderUrl(startUrl):
                break
            else:
                print("invalid GoodReader address!")
        print("start scraping " + startUrl + " !!!")
        scraping(startUrl)

    # DELETE
    elif result == 6:
        while 1 > 0:
            print("Which object you want to delete? Author or Book")
            command = input('>')
            if command == "Author":
                deleteTarget = "Author"
                break
            elif command == "Book":
                deleteTarget = "Book"
                break
            else:
                print("please enter valid object")
        while 1 > 0:
            print("Enter object id?")
            command = input('>')
            if len(command) != 0:
                deleteId = int(command)
                break
            else:
                print("please enter valid id")
        deleteHelper(deleteTarget, deleteId)
