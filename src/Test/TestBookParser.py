from src.WebScraper import BookParser

# This file tests whether the BookParse correctly handles scraping data
if __name__ == '__main__':
    # Check First book
    firstBook = BookParser.Book("https://www.goodreads.com/book/show/3735293-clean-code?from_search=true&qid=HhMDV0vMa5&rank=1")
    firstUrl = firstBook.getBookUrl()
    assert firstUrl == "https://www.goodreads.com/book/show/3735293-clean-code?from_search=true&qid=HhMDV0vMa5&rank=1"
    firstTitle  = firstBook.getTitle()
    assert firstTitle == "Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin"
    firstId = firstBook.getBookId()
    assert firstId == "3735293"
    firstISBN = firstBook.getISBN()
    assert firstISBN == "9780132350884"
    firstAuthorUrl = firstBook.getAuthorUrl()
    assert firstAuthorUrl == "https://www.goodreads.com/author/show/45372.Robert_C_Martin"
    firstAuthor = firstBook.getAuthor()
    assert firstAuthor == "Robert C. Martin"
    firstRating = firstBook.getRating()
    firstRatingCount = firstBook.getRatingCount()
    assert firstRatingCount == "15936"
    firstReviewCount = firstBook.getReviewCount()
    assert firstReviewCount == "950"
    firstImageUrl = firstBook.getBookImageUrl()
    assert firstImageUrl == "https://www.goodreads.com/book/photo/3735293-clean-code"
    listOfFirstSimilarBooksName, listOfFirstSimilarBooksUrl = firstBook.getSimilarBooks()
    print(listOfFirstSimilarBooksUrl)
    print(listOfFirstSimilarBooksName)
    # Check visually

    # Second book
    secondBook = BookParser.Book("https://www.goodreads.com/book/show/141565.This_Is_Your_Brain_on_Music")
    secondUrl = secondBook.getBookUrl()
    assert secondUrl == "https://www.goodreads.com/book/show/141565.This_Is_Your_Brain_on_Music"
    secondTile = secondBook.getTitle()
    assert secondTile == "This Is Your Brain on Music: The Science of a Human Obsession by Daniel J. Levitin"
    secondId = secondBook.getBookId()
    assert secondId == "141565"
    secondISBN = secondBook.getISBN()
    assert secondISBN == "9780525949695"
    secondAuthorUrl = secondBook.getAuthorUrl()
    assert secondAuthorUrl == "https://www.goodreads.com/author/show/81619.Daniel_J_Levitin"
    secondAuthor = secondBook.getAuthor()
    assert secondAuthor == "Daniel J. Levitin"
    secondRating = secondBook.getRating()
    secondRatingCount = secondBook.getRatingCount()
    assert secondRatingCount == "54845"
    secondReviewCount = secondBook.getReviewCount()
    assert secondReviewCount == "1594"
    secondImageUrl = secondBook.getBookImageUrl()
    assert secondImageUrl == "https://www.goodreads.com/book/photo/141565.This_Is_Your_Brain_on_Music"
    listOfSecondSimilarBooksName, listOfSecondSimilarBooksUrl = secondBook.getSimilarBooks()
    print(listOfSecondSimilarBooksUrl)
    print(listOfSecondSimilarBooksName)
    # Check visually
