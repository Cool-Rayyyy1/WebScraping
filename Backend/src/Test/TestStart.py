from src.WebScraper import start

# This file tests the functions of the start.py
if __name__ == '__main__':
    # First run the main for the start.py manually and go to mysql workbench to see if the table has been created
    # Besides, the terminal should requires user to enter parameters, try some valid parameters and invalid parameters.
    firstResult = start.checkGoodReaderUrl(
        "https://www.goodreads.com/book/show/3735293-clean-code?from_search=true&qid=HhMDV0vMa5&rank=1")
    assert firstResult == True
    secondResult = start.checkGoodReaderUrl("https://wiki.illinois.edu/wiki/display/cs242/Home")
    assert secondResult == False
    # Then we need to check whether duplicates will appear in the database
    start.startScraping()
    # Then go to dabase and check the correct number of author and books without duplicates.
