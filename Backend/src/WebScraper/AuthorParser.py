import requests
from bs4 import BeautifulSoup

# Author is a class that used to scraping all kinds of necessary information of current author website
class Author:
    # Constructor
    def __init__(self, url):
        self.url = url
        self.soup = BeautifulSoup(requests.get(self.url).content, "html.parser")

    # Below methods are all kinds of helper function to scrap data.
    def getName(self):
        try:
            return str(self.soup.find("span", itemprop="name").text)
        except:
            print("Can not scrape author name")
            return None

    def getAuthorUrl(self):
        return str(self.url)

    def getAuthorId(self):
        idName = self.url.split('/')[5]
        id = idName.split('.')[0]
        return id

    def getRating(self):
        try:
            return self.soup.find("span", attrs={"class", "average"}, itemprop="ratingValue").text
        except:
            print("Can not scrape rating")
            return None

    def getRatingCount(self):
        try:
            return self.soup.find("span", attrs={"class", "value-title"}, itemprop="ratingCount").get("content")
        except:
            print("Can not scrape ratingCount")
            return None

    def getReviewCount(self):
        try:
            return self.soup.find("span", attrs={"class", "value-title"}, itemprop="reviewCount").get("content")
        except:
            print("Can not scrape reviewCount")
            return None

    def getImageUrl(self):
        try:
            imageUrl = self.soup.find("a", title=self.getName(), rel="nofollow").get("href")
            return str("https://www.goodreads.com" + imageUrl)
        except:
            print("Can not scrape ImageUrl")
            return None

    def getRelatedAuthors(self):
        try:
            soup = self.getSimilarAuthorsSoup()
            list = []
            for tag in soup.find_all("span", itemprop="name"):
                if not tag.text == self.getName():
                    list.append(tag.text)
            return list
        except:
            print("Can not scrape RelatedAuthors")
            return None

    def getSimilarAuthorsSoup(self):
        url = "https://www.goodreads.com/author/similar/" + self.getAuthorId() + "." \
                                    + self.getName().replace(".", "").replace(" ", "_")
        relatedAuthorsPage = requests.get(url)
        relatedAuthorsSoup = BeautifulSoup(relatedAuthorsPage.content, "html.parser")
        return relatedAuthorsSoup

    def getAuthorsBooks(self):
        try:
            list = []
            for tag in self.soup.find_all("span", itemprop="name", role="heading"):
                list.append(tag.text)
            return list
        except:
            print("Can not scrape author books")
            return None