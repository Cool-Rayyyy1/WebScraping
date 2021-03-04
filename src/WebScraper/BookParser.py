import requests
from bs4 import BeautifulSoup

# Book is a class that used to scraping all kinds of necessary information of current book website
class Book:
    # Constructor
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(self.url).content, "html.parser")

    # Below methods are all kinds of helper function to scrap data.
    def getBookUrl(self):
        return str(self.url)

    def getTitle(self):
        try:
            return str(self.soup.title.string)
        except:
            print("Can not scrape book title!")
            return None

    def getBookId(self):
        idName = self.url.split('/')[5]
        id1 = idName.split('.')[0]
        id2 = idName.split('-')[0]
        if id2.isnumeric():
            return id2
        else:
            return id1

    def getISBN(self):
        try:
            return str(self.soup.find("span", itemprop="isbn").text)
        except:
            print("Can not scrape book title")
            return None

    def getAuthorUrl(self):
        try:
            authorUrl = self.soup.find("a", attrs={"class", "authorName"}, itemprop="url").get("href")
            return str(authorUrl)
        except:
            print("Can not scrape author url")
            return None

    def getAuthor(self):
        try:
            return str(self.soup.find("span", itemprop="name").text)
        except:
            print("Can not scrape author name")
            return None

    def getRating(self):
        try:
            return str(self.soup.find("span", itemprop="ratingValue").text.replace(' ', ''))
        except:
            print("Can not scrape rating")
            return None

    def getRatingCount(self):
        try:
            return str(self.soup.find("meta", itemprop="ratingCount").get("content"))
        except:
            print("Can not scrape reviewCount")
            return None

    def getReviewCount(self):
        try:
            return str(self.soup.find("meta", itemprop="reviewCount").get("content"))
        except:
            print("Can not scrape reviewCount")
            return None

    def getBookImageUrl(self):
        try:
            imageUrl = self.soup.find("a", itemprop="image", rel="nofollow").get("href")
            return str("https://www.goodreads.com" + imageUrl)
        except:
            print("Can not scrape imageUrl")
            return None

    def getSimilarBooks(self):
        try:
            similarUrl = self.soup.find("a", attrs={"class", "actionLink right seeMoreLink"}).get("href")
            similarSoup = BeautifulSoup(requests.get(similarUrl).content, "html.parser")
            books = similarSoup.find_all(attrs={"class", "listWithDividers__item"})
            nameList = []
            urlList = []
            originalName = self.getTitle().split("by")[0]
            size = len(originalName) - 1
            targetName = originalName[:size]
            for book in books:
                bookName = book.find("span", itemprop="name").text
                bookUrl = "https://www.goodreads.com" + book.find("a", attrs={"class", "gr-h3 gr-h3--serif gr-h3--noMargin"}, itemprop="url").get("href")
                if bookName != targetName:
                    nameList.append(bookName)
                    urlList.append(bookUrl)
            return nameList, urlList
        except:
            print("Can not find similarBooks")
            return None, None






