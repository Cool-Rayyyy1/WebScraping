from src.WebScraper import start
from src.WebScraper import JsonParser

# This files is hard to test but basically checks if JsonParser class could normally work
if __name__ == '__main__':
    # First create a instance of JsonParser to connects to sql server
    parser = JsonParser.jsonParser();
    # Then we need to run the start Web scraping to ensure we have data in sql server
    # manually run the main for start.py
    start.startScraping()
    # Right now the json file is empty, we could test whether write function could catch the error of empty json list
    parser.writeBookData()
    parser.commitChange()
    # Error should be printed
    parser.writeAuthorData()
    parser.commitChange()
    # Error should be printed again
    # Then we should have data right now we could dump data from tables
    parser.exportBookData()
    parser.commitChange()
    parser.exportAuthorData()
    parser.commitChange()
    # This could be tested by opening the json file to check whether data has been saved. Then we could test write functions
    # Recreate the table
    parser.c.execute('''DROP TABLE Book''')
    parser.c.execute('''CREATE TABLE Book(
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
    parser.c.execute('''Drop TABLE Author''')
    parser.c.execute('''CREATE TABLE Author(
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
    parser.writeBookData()
    # Right now, if we go to the book table in mysql workbench, data should be there
    parser.writeAuthorData()
    # Right now, if we go to the book table in mysql workbench, data should be there
    # Finish test
