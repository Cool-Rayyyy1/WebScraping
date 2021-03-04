import json
import sys
import mysql.connector
from src.WebScraper import AuthorParser, BookParser

# some global variables that are used to determine when to stop scraping and check for duplicates
targetBook = 0
targetAuthor = 0
countBook = 0
countAuthor = 0
myset = set()

# Helper function to set global targetBook
def setTargetBook(numberOfBook):
    global targetBook
    targetBook = numberOfBook

# Helper function to set global targetAuthor
def setTargetAuthor(numberOfAuthor):
    global targetAuthor
    targetAuthor = numberOfAuthor

# Helper function to increase global countBook
def bookIncrement():
    global countBook
    countBook += 1

# Helper function to increase global countAuthor
def authorIncrement():
    global countAuthor
    countAuthor += 1

# Helper function to check duplicates
def checkExist(element):
    global myset
    if element in myset:
        return True
    else:
        return False

# Helper function to add name into set
def addName(element):
    global myset
    myset.add(element)

# Helper function to check if the url points to a book goodReader website
def checkGoodReaderUrl(url):
    if "goodreads.com/book/show/" in url:
        return True
    else:
        return False

# Main function to start Scraping
def startWebScraping(currentUrl):
    ## stop running
    if countBook == targetBook:
        sys.exit()

    ## create instances
    currentBook = BookParser.Book(currentUrl)
    currentAuthor = AuthorParser.Author(currentBook.getAuthorUrl())
    currentConn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
    current = currentConn.cursor()

    ## store book information
    bookUrl = currentBook.getBookUrl()
    bookName = currentBook.getTitle()
    print("start scraping " + bookName + " !")
    addName(bookName)
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
    current.execute('''INSERT INTO Book VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
    bookUrl, bookName, bookId, bookISBN, authorUrl, authorName, bookRating, bookRatingCount, bookReviewCount,
    bookImageUrl, jsonOfSimilar))
    bookIncrement()

    ## store author information
    if countAuthor < targetAuthor:
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
        current.execute('''INSERT INTO Author VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
        authorName, authorUrl, authorId, authorRating, authorRatingCount, authorReviewCount, authorImageUrl,
        jsonOfRelated, jsonOfAuthorBooks))
        authorIncrement()

    ## prepare for next iteration
    currentConn.commit()
    if similarBook is None and similarUrl is None:
        return
    else:
        for i in range(len(similarUrl)):
            nextBook = BookParser.Book(similarUrl[i])
            if checkExist(nextBook.getTitle()):
                continue
            startWebScraping(similarUrl[i])

# Main function to get information from user
def startScraping():
    while 1 > 0:
        print("Please enter a valid GoodReader address!")
        startUrl = input('>')
        if checkGoodReaderUrl(startUrl):
            break
        else:
            print("invalid GoodReader address!")
    while 1 > 0:
        while 1 > 0:
            print("Please enter the number of books you want to scrape!")
            numOfBook = input('>')
            if int(numOfBook) <= 30:
                print("At least 200 books are required!")
            else:
                print("Warning! you choose more than 200 books!")
                break
        while 1 > 0:
            print("Please enter the number of authors you want to scrape!")
            numOfAuthor = input('>')
            if int(numOfAuthor) <= 20:
                print("At least 50 authors are required!")
            else:
                print("Warning! you choose more than 50 authors!")
                break

        if int(numOfBook) + int(numOfAuthor) > 2000:
            print("You can not scrape 2000 books or authors")
        else:
            break
    # get all the information
    setTargetBook(int(numOfBook))
    setTargetAuthor(int(numOfAuthor))
    startWebScraping(startUrl)


if __name__ == '__main__':
    # connect to sql server
    conn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
    c = conn.cursor()

    # create table
    c.execute('''DROP TABLE Book''')
    c.execute('''CREATE TABLE Book(
            book_url VARCHAR(2083), 
            title VARCHAR(255),
            book_id VARCHAR(99), 
            ISBN VARCHAR(13), 
            author_url VARCHAR(2083),
            author VARCHAR(255),
            rating VARCHAR(11),
            rating_count VARCHAR(11), 
            review_count VARCHAR(11), 
            image_url VARCHAR(2083), 
            similar_books JSON
    )''')
    c.execute('''Drop TABLE Author''')
    c.execute('''CREATE TABLE Author(
            name VARCHAR(255),
            author_url VARCHAR(2083),
            author_Id VARCHAR(13),
            rating VARCHAR(11),
            rating_count VARCHAR(11),
            review_count VARCHAR(11),
            image_url VARCHAR(2083),
            related_author JSON,
            author_books JSON
    )''')
    conn.commit()
    startScraping()
