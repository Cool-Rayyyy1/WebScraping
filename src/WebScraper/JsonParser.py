import mysql.connector
import json


# jsonParser is a class that are used to export data from sql server and save as json file or write data into sql server
class jsonParser:
    # Constructor
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
        self.c = self.conn.cursor()

    # Method for exporting data from authorFile.json
    def exportAuthorData(self):
        self.c.execute('''SELECT * FROM author''')
        columns = [col[0] for col in self.c.description]
        rows = [dict(zip(columns, row)) for row in self.c.fetchall()]
        with open("authorFile.json", "w") as writeFile:
            json.dump(rows, writeFile)

    # Method for exporting data from bookFile.json
    def exportBookData(self):
        self.c.execute('''SELECT * FROM book''')
        columns = [col[0] for col in self.c.description]
        rows = [dict(zip(columns, row)) for row in self.c.fetchall()]
        with open("bookFile.json", "w") as writeFile:
            json.dump(rows, writeFile)

    # Method for writing json file data into author table
    def writeAuthorData(self):
        self.c.execute('''Drop TABLE Author''')
        self.c.execute('''CREATE TABLE Author(
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
        try:
            with open("authorFile.json", "r") as readFile:
                authorData = json.load(readFile)
                if isinstance(authorData, list):
                    for item in authorData:
                        valueDicList = item.values()
                        valueList = list(valueDicList)
                        self.c.execute('''INSERT INTO Author VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                            valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5],
                            valueList[6],
                            valueList[7], valueList[8]))
                else:
                    print("Can not load List type from Json file!")
        except:
            print("Invalid Json file")

    # Method for writing json file data into book table
    def writeBookData(self):
        self.c.execute('''Drop TABLE Book''')
        self.c.execute('''CREATE TABLE Book(
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
        try:
            with open("bookFile.json", "r") as readFile:
                bookData = json.load(readFile)
                if isinstance(bookData, list):
                    for item in bookData:
                        valueDicList = item.values()
                        valueList = list(valueDicList)
                        self.c.execute('''INSERT INTO Book VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (
                            valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5],
                            valueList[6],
                            valueList[7], valueList[8], valueList[9], valueList[10]))
                else:
                    print("Can not load List type from Json file!")

        except:
            print("Invalid Json file")

    # Method for closing connection
    def commitChange(self):
        self.conn.commit()


if __name__ == '__main__':
    parser = jsonParser();
    parser.writeBookData();
    parser.commitChange()
