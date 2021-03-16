# Manual Test Plan
This Maunal Test Plan included the Test plan for the Frontend and Backend<br>
## Prerequisites
Frontend:<br>
Editor: Visual Studio Code<br>
Language：Node.js (React FrameWork)<br>
Backend:<br>
Editor: PyCharm Community Edition<br>
Packages: beautifulsoup4, mysql, mysql-connector-python,  requests.<br>
DataBase: Mysql
## Environment Setup and configurations

* For the FrontEnd, you need to install the create-react-app at the frontend folder by npx create-react-app (Your app name)
  * Then you need to install the package semantic-ui-react by npm install semantic-ui-react
  * Then you could start the Frontend by using the command npm start or npx start.<br>

* For the Backend, You should open and create a new project on Intellij.<br>
  * Right Click the src/WebScraper/start.py file and click the Run "start.py.main()" button in the middle of the menu that has been popped out to run the GUI.
  * Then the web scraping will begin by running the startScraping method and user need to enter a valid GoodReader website and two valid number of Books and authors that the user want to scrape.
  Otherwise, an error will display and user need to enter the valid address or number again to start web scraping
## Operations, Results, and the Error Messages
For the Frontend: there are basically 5 aspects that needed to be tested!<br>
### 1. The Start Page: index.jsx and App.js
This could be directly tested by starting the Frontend Projects using the command npm start at the right path! Then you should see the welcome page which is the main page. This should be Tested by clicking all different links on the main page to check whether routes has successfully executed. If the user enters a invalid localhost website, the routes should be redirected to the 404 Not found page. All the mentioned places should be tested!<br>
### 2. The Get API request
This Test should tests all the relevant GET API by clicling in to the corresponding get webpages. 
* For the first getBooksAll and getAuthorsAll jsx files, after clicking the main page, it should be jumps to its corresponding webpages and parts of the information of current books and authors held in the database should be printed out. This could be tested by openning the database and check each one.
* For the normal getBook and getAuthor API, the webpage will require the user to enter the id of the book or the author. After clicking the button, the correspoding searching results will be shown on the page. If the Author or the Book does not exist, the information will not be printed out! And user must enter a valid id in order to search for the book and author. 
* At last, the search API will require users to enter the complex query in order to search the book and author.
If the book or author does not exist, then the information will not show up.<br>
### 3. The Put API request
This Test should tests two PUT API which are the putAuthor.jsx and the putBook.jsx
* For the putAuthor.jsx, the webpae requires the user to enter the id of the author, so the API could search the author that the user want to change. Besides, the user also need to enter the field for the API and the value they want to update. After doing this, clicking the button, the API will do the rest for them. Once the update has succeed, the message will remind the users. And the aspect that if the field or Author does not exist should also be tested. The returend message will indicate the result.
* For the putBook.jsx, basically the tests are the same with the putAuthor.jsx
### 4. The POST API request
This test should tests two POST API which are the postAuthor.jsx and the postBook.jsx
* For the postAuthor.jsx, the webpage requires the user to enter the all the fileds of the author, so the API could totally create a bran-new author information in the database. After doing this, clicking the button, the API will do the rest for them. Once the creating process has succeed, the message will poped out to remind the users. And the aspect that if the one of the field or Author does not exist should also be tested. The returend message will indicate the result.
* For the postBook.jsx, basically the tests are the same with the postAuthor.jsx
### 5. The Delete API request
This test should tests two DELETE API which are the deleteAuthor.jsx and the deleteBook.jsx
* For the deleteAuthor.jsx, the webpage requires the user to enter the id of the author that they want to delete in the database. And then, after doing this, the user just need to click the button and API will do the rest for them. This could be checked by clicking the getAuthorAll page from the mainPage. Besides, if the author that user want to delte does not exist, then the corresponding message will occur to remind the user which could be tested by entering a non-exist id of author.
* For the deleteBook.jsx, basically the tests are the same with the deleteAuthor.jsx<br>
For the Backend: there are basically four files that need to be tested!<br>
### 1. AuthorParser.py
The AuthorParser.py contains a python class Author that connects the author webpage and owns various methods to scrape the necessary data.<br>
* AuthorParser has method to scrape the author name, author url, author id, rating, rating count, review count, image url, related authors, and author books.
These methods will return these variables with corresponding types. The returned results should be checked by printing on the terminal and check the correctness.
  For example, pasting the image url returned by the method and jumps to that website to check if the image has been shown.<br>
* Also need to handle the errors correctly, if the method could not scrape the information that are missing, null should be returned and corresponding error messages will be printed out.
This needs to be tested if null has been correctly returned and error messages will be displayed in the terminal.
  
### 2. BookParser.py
The BookParser.py contains a python class Book that connects the book webpage and owns various methods to scrape the necessary data.<br>
* BookParser has method to scrape the book url, book title, book id, ISBN, author url, author name, rating, rating count, review count, image url, and similar books.
These methods will return these variables with corresponding types. The returned results should be checked by printing on the terminal and check the correctness.
  For example, pasting the author url returned by the method and jumps to that website to check if the method returned correct author url.<br>
* Also need to handle the errors correctly, if the method could not scrape the information that are missing, null should be returned and corresponding error messages will be printed out.
This needs to be tested if null has been correctly returned and error messages will be displayed in the terminal. Besides, the similar books should be handled carefully and checked to avoid segmentation fault.
  If the method can not find the similar books, null should be returned, and the current iteration should be finished and jumps to the next iteration of previous call's loop.
  
### 3. JsonParser.py
The JsonParser.py contains a python class jsonParser that handles how to export data from my sql database and save these data as json file or read data from valid Json file and write it into sql database.
* JsonParser has four five main methods and are responsible for the functions mentioned previously.<br>
* Each function should be checked. The basic tests is to check export function could pop and get data from sql server and successfully change data to list type and dumps into json file.
This could be directly tested by clicking the json file and check the data shown on these files. Besides, the function to read from the json file and write into the database should also be checked.
  This could be tested by first export some data from server and use these data stored in the json file to call write functions. Opening the sql server and check whether these data has been added.<br>
* Error also need to be checked. The error message should be displayed when invalid Json files has been passed in.

### 4. start.py
The start.py contains the method to start a web scraping that handles the beginning of the scraping til the ends of the scraping. There are several aspects that need to be checked.
* First, whether the main function connects to the sql server and the author and book table has been created needs to be checked. This can be done by directly go to mysql workbench to check.
* Second, when the user start to write the inputs for the start url, numOfBook, and numOfAuthor, valid parameters should be checked and corresponding error messages should be printed out to remind users. Util all three
valid parameters has been gathered, the web scraping could start.
* Third, the scraping process should be run correct times which means the database should has the correct number of rows. This could be done by checking whether those global variables has been correctly checked and handled.
* Fourth, some small details need also to be checked. For example, whether the function has been correctly run fixed times and no error appear during running. Besides, no duplications appear in the database.
  