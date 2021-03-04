# sp21-cs242-assignment2.0
Due date: :crescent_moon: 23:59 CDT March 2, 2021 :clock12: 
### Part 0: Reading
:round_pushpin:<br>
Before you begin web scraping, make sure to read the following links:
* https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/
* https://www.promptcloud.com/blog/dont-get-blacklisted-legitimate-web-scraping-process
* https://www.promptcloud.com/blog/some-traps-to-avoid-in-web-scraping/
### Part I: Web Scraping
:round_pushpin:<br>
* Gather information of Authors and Books from Goodreads.
  * You should gather information from a large number of book pages (>200) and authors pages (>50) Essentially saying you need to contain at least information of at least 200 books and 50 authors. You should not go beyond 2000 books or authors. 
  * The starting page must be a book page. The starting page should be a variable and should not be hard-coded. (For example, starting from clean code: https://www.goodreads.com/book/show/3735293-clean-code). The order of traversal doesn't matter: for example, you can find next books to scrape by visiting all books that the same authors have written, or you can just use similar books listed in the GoodReads website.
* Report progress and exceptions (e.g., books without ISBN). There is no limit as to how this should be implemented.
* Represent Books and Authors efficiently. There is no one structure for this assignment, and there are no type constraints for fields.
### Part2 Data Storage in an External Database
:round_pushpin:<br>
In the third part of this assignment, we will be using the same scraper you build in part one and store data into a database. We do not have a constraint in the type of database you are using, Here are some suggestions:
* mongoDB (including mongoDB Altas) + PyMongo
* firebase
* SQLite
* MySQL

### Part3 Command Line Interface
:round_pushpin:<br>
To make the scrapers more versatile, we can write a simple command line interface that allows other users to configure behaviors of the program. In this assignment, you are only required to take user inputs through command line arguments (however, you will need to make the program interactive by next assignment). Python for instance now has several built-in/external packages to assist this process (for example, the argparse library). It can handle and complete simple preprocessing of the arguments a user provided to the system.
Your program should be able to:
* Accept any valid starting URL
  * Check if the URL is valid, if it points to GoodReads, if it potentially represents a book
* Accept an arbitrary number of books and authors to scrape
  * Print warning for numbers greater than 200 books and 50 authors
* Read from JSON files to create new books / authors or update existing books / authors  
  * Print error for invalid JSON file (e.g., syntax error) and malformed data structure (e.g., what if the JSON is an array, or if the object doesn't have id). Discuss your design choice during discussions
  * Print what new entries are updated or created
* Export existing books / authors into JSON files
  * The output must be valid JSON

### Part IV: Miscellaneous Requirements    
:round_pushpin:<br>
As usual, we require that you write extensive unit tests for each part of this assignment. We understand that it can be difficult to test for web scraping. However, make sure to exhaustively test all other parts of your code. If your language does not have a testing framework (unlikely), you will need to implement your own test runner and utilities to accomplish this part of the assignment. In order to test your web scraper, your moderator will ask you to scrape a book page of their choice in section, so be prepared. You should also be demoing your data storage.