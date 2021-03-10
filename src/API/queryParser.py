import mysql.connector


# This class is used to parse the complex query when api faced with such parameters to help api find proper result in the database
class Query:
    # The constructor for the Query class
    def __init__(self, inputQuery):
        self.query = inputQuery
        self.conn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
        self.c = self.conn.cursor(buffered=True)

    # Calling this method will start parse each Query class's query
    def startParsing(self):
        # First check field
        if self.query.find('.') == -1:
            return dict(error="You need to specify . for the field")
        fieldContent = self.query.split('.', 1)
        target = fieldContent[0]
        restQuery = fieldContent[1]
        queryDict = {}
        # Then check proper parameters
        try:
            if target == "book":
                queryDict["target"] = "book"
            elif target == "author":
                queryDict["target"] = "author"
            else:
                return dict(error="You must enter a book or a author")
            if restQuery.find(':') == -1:
                return dict(error="You need to specify : for the field")
            field = restQuery.split(':', 1)[0]
            content = restQuery.split(':', 1)[1]
            queryDict["field"] = field
            queryDict["content"] = content
        except Exception:
            return dict(error="Invalid object or field")
        # Then we need to check logical operator
        operatorResult = self.checkOperators(queryDict)
        if "error" in queryDict:
            return operatorResult
        elif queryDict["operator"] == "AND":
            return self.findAndOr(operatorResult, 1)
        elif queryDict["operator"] == "OR":
            return self.findAndOr(operatorResult, 0)
        elif queryDict["operator"] == "NOT":
            return self.findNot(operatorResult, operatorResult["field"], operatorResult["first"])
        elif queryDict["operator"] == ">":
            return self.findGreatOrLess(operatorResult, 1)
        elif queryDict["operator"] == "<":
            return self.findGreatOrLess(operatorResult, 0)
        else:
            return self.findContent(operatorResult, operatorResult["field"], operatorResult["content"])

    # This method will handle the case when operator is > or <
    # indicator = 1 for > indicator = 0 for <
    def findGreatOrLess(self, queryDict, indicator):
        # > greater category
        if queryDict["target"] == "book":
            if queryDict["field"] == "book_id":
                value = int(queryDict["first"])
                sql = "SELECT book_id FROM Book"
                self.c.execute(sql)
                self.conn.commit()
                tempList = self.c.fetchall()
                compareList = []
                for data in tempList:
                    compareList.append(int(data[0]))
                finalList = []
                for data in compareList:
                    if indicator == 1:
                        if data > value:
                            finalList.append(data)
                    else:
                        if data < value:
                            finalList.append(data)
                searchList = []
                for data in finalList:
                    searchList.append(str(data))
                returnList = []
                for each in searchList:
                    searchSql = "SELECT * FROM Book WHERE book_id = %s"
                    target = (each,)
                    self.c.execute(searchSql, target)
                    self.conn.commit()
                    searchResult = self.c.fetchall()
                    returnList.append(searchResult[0])
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
            elif queryDict["field"] == "ISBN":
                value = float(queryDict["first"])
                sql = "SELECT book_id, ISBN FROM Book"
                if indicator == 1:
                    returnList = self.greatOrLessHelperBook(sql, value, 1)
                else:
                    returnList = self.greatOrLessHelperBook(sql, value, 0)
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
            elif queryDict["field"] == "rating":
                value = float(queryDict["first"])
                sql = "SELECT book_id, rating FROM Book"
                if indicator == 1:
                    returnList = self.greatOrLessHelperBook(sql, value, 1)
                else:
                    returnList = self.greatOrLessHelperBook(sql, value, 0)
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
            elif queryDict["field"] == "rating_count":
                value = float(queryDict["first"])
                sql = "SELECT book_id, rating_count FROM Book"
                if indicator == 1:
                    returnList = self.greatOrLessHelperBook(sql, value, 1)
                else:
                    returnList = self.greatOrLessHelperBook(sql, value, 0)
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
            elif queryDict["field"] == "review_count":
                value = float(queryDict["first"])
                sql = "SELECT book_id, review_count FROM Book"
                if indicator == 1:
                    returnList = self.greatOrLessHelperBook(sql, value, 1)
                else:
                    returnList = self.greatOrLessHelperBook(sql, value, 0)
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
        else:
            # Author category
            if queryDict["field"] == "authorId":
                value = int(queryDict["first"])
                sql = "SELECT author_Id FROM Author"
                self.c.execute(sql)
                self.conn.commit()
                tempList = self.c.fetchall()
                compareList = []
                for data in tempList:
                    compareList.append(int(data[0]))
                finalList = []
                for data in compareList:
                    if indicator == 1:
                        if data > value:
                            finalList.append(data)
                    else:
                        if data < value:
                            finalList.append(data)
                searchList = []
                for data in finalList:
                    searchList.append(str(data))
                returnList = []
                for each in searchList:
                    searchSql = "SELECT * FROM Author WHERE author_Id = %s"
                    target = (each,)
                    self.c.execute(searchSql, target)
                    self.conn.commit()
                    searchResult = self.c.fetchall()
                    returnList.append(searchResult[0])
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
            elif queryDict["field"] == "rating":
                value = float(queryDict["first"])
                sql = "SELECT author_Id, rating FROM Author"
                if indicator == 1:
                    returnList = self.greatOrLessHelperAuthor(sql, value, 1)
                else:
                    returnList = self.greatOrLessHelperAuthor(sql, value, 0)
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
            elif queryDict["field"] == "rating_count":
                value = float(queryDict["first"])
                sql = "SELECT author_Id, rating_count FROM Author"
                if indicator == 1:
                    returnList = self.greatOrLessHelperAuthor(sql, value, 1)
                else:
                    returnList = self.greatOrLessHelperAuthor(sql, value, 0)
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList
            elif queryDict["field"] == "review_count":
                value = float(queryDict["first"])
                sql = "SELECT author_Id, review_count FROM Author"
                if indicator == 1:
                    returnList = self.greatOrLessHelperAuthor(sql, value, 1)
                else:
                    returnList = self.greatOrLessHelperAuthor(sql, value, 0)
                if len(returnList) == 0:
                    return dict(error="No such item exist!")
                return returnList

    # This method helps the findGreatOrLess method to find proper data in author table which avoid mass duplication
    def greatOrLessHelperAuthor(self, sql, value, indicator):
        self.c.execute(sql)
        self.conn.commit()
        tempList = self.c.fetchall()
        compareList = []
        for data in tempList:
            compareList.append((data[0], float(data[1])))
        finalList = []
        for data in compareList:
            if indicator == 0:
                if data[1] < value:
                    finalList.append(data[0])
            else:
                if data[1] > value:
                    finalList.append(data[0])
        returnList = []
        for each in finalList:
            searchSql = "SELECT * FROM Author WHERE author_Id = %s"
            target = (each,)
            self.c.execute(searchSql, target)
            self.conn.commit()
            searchResult = self.c.fetchall()
            returnList.append(searchResult[0])
        return returnList

    # This method helps the findGreatOrLess method to find proper data in book table which avoid mass duplication
    def greatOrLessHelperBook(self, sql, value, indicator):
        self.c.execute(sql)
        self.conn.commit()
        tempList = self.c.fetchall()
        compareList = []
        for data in tempList:
            compareList.append((data[0], float(data[1])))
        finalList = []
        for data in compareList:
            if indicator == 0:
                if data[1] < value:
                    finalList.append(data[0])
            else:
                if data[1] > value:
                    finalList.append(data[0])
        returnList = []
        for each in finalList:
            searchSql = "SELECT * FROM Book WHERE book_id = %s"
            target = (each,)
            self.c.execute(searchSql, target)
            self.conn.commit()
            searchResult = self.c.fetchall()
            returnList.append(searchResult[0])
        return returnList

    # This method will help to handle the and or cases
    # Indicator = 1 for and category and 0 for or category
    def findAndOr(self, queryDict, indicator):
        if indicator == 1:
            # And category
            secondField = queryDict["second"].split(':', 1)[0]
            secondContent = queryDict["second"].split(':', 1)[1]
            firstResult = self.findContent(queryDict, queryDict["field"], queryDict["first"])
            secondResult = self.findContent(queryDict, secondField, secondContent)
            if len(firstResult) == 0 or len(secondResult) == 0:
                return dict(error="No such item exist!")
            finalList = []
            for x in firstResult:
                for y in secondResult:
                    if x == y:
                        finalList.append(x)
                        break
            if len(finalList) != 0:
                return finalList
            else:
                return dict(error="No such item exist!")
        else:
            # Or category
            secondField = queryDict["second"].split(':', 1)[0]
            secondContent = queryDict["second"].split(':', 1)[1]
            firstResult = self.findContent(queryDict, queryDict["field"], queryDict["first"])
            secondResult = self.findContent(queryDict, secondField, secondContent)
            if len(firstResult) == 0 or len(secondResult) == 0:
                return dict(error="No such item exist!")
            finalList = []
            for x in firstResult:
                finalList.append(x)
            for y in secondResult:
                finalList.append(y)
            return finalList

    # This method handles not cases to find all the proper data in database
    def findNot(self, queryDict, field, content):
        target = (content,)
        if queryDict["target"] == "book":
            # book category
            if field == "book_id":
                sql = "SELECT * FROM Book WHERE book_id != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "book_url":
                sql = "SELECT * FROM Book WHERE book_url != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "title":
                sql = "SELECT * FROM Book WHERE title != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "ISBN":
                sql = "SELECT * FROM Book WHERE ISBN != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "author_url":
                sql = "SELECT * FROM Book WHERE author_url != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "author":
                sql = "SELECT * FROM Book WHERE author != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating":
                sql = "SELECT * FROM Book WHERE rating != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating_count":
                sql = "SELECT * FROM Book WHERE rating_count != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "review_count":
                sql = "SELECT * FROM Book WHERE review_count != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "image_url":
                sql = "SELECT * FROM Book WHERE image_url != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
        else:
            # author category
            if field == "authorId":
                sql = "SELECT * FROM Author WHERE author_ID != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "name":
                sql = "SELECT * FROM Author WHERE name != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "author_url":
                sql = "SELECT * FROM Author WHERE author_url != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating":
                sql = "SELECT * FROM Author WHERE rating != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating_count":
                sql = "SELECT * FROM Author WHERE rating_count != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "review_count":
                sql = "SELECT * FROM Author WHERE review_count != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "image_url":
                sql = "SELECT * FROM Author WHERE image_url != %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()

        if len(finalContent) == 0:
            return dict(error="No such item exist!")

        return finalContent

    # This method handles when the query does not contain any special operator, need to directly find the result
    def findContent(self, queryDict, field, content):
        # first check whether contains ""
        if queryDict["operator"] != "AND" and queryDict["operator"] != "OR":
            if queryDict["content"].count('"') != 2:
                return dict(error="You need to have proper '' in your search!")
        content = content.replace('"', "")
        target = (content,)
        if queryDict["target"] == "book":
            # book category
            if field == "book_id":
                sql = "SELECT * FROM Book WHERE book_id = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "book_url":
                sql = "SELECT * FROM Book WHERE book_url = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "title":
                sql = "SELECT * FROM Book WHERE title = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "ISBN":
                sql = "SELECT * FROM Book WHERE ISBN = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "author_url":
                sql = "SELECT * FROM Book WHERE author_url = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "author":
                sql = "SELECT * FROM Book WHERE author = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating":
                sql = "SELECT * FROM Book WHERE rating = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating_count":
                sql = "SELECT * FROM Book WHERE rating_count = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "review_count":
                sql = "SELECT * FROM Book WHERE review_count = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "image_url":
                sql = "SELECT * FROM Book WHERE image_url = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
        else:
            # author category
            if field == "authorId":
                sql = "SELECT * FROM Author WHERE author_ID = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "name":
                sql = "SELECT * FROM Author WHERE name = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "author_url":
                sql = "SELECT * FROM Author WHERE author_url = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating":
                sql = "SELECT * FROM Author WHERE rating = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "rating_count":
                sql = "SELECT * FROM Author WHERE rating_count = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "review_count":
                sql = "SELECT * FROM Author WHERE review_count = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()
            elif field == "image_url":
                sql = "SELECT * FROM Author WHERE image_url = %s"
                self.c.execute(sql, target)
                self.conn.commit()
                finalContent = self.c.fetchall()

        if len(finalContent) == 0:
            return dict(error="No such item exist!")

        return finalContent

    # This method helps to deal with different cases and put each part of query to corresponding places
    def checkOperators(self, queryDict):
        try:
            if " AND " in queryDict["content"]:
                queryDict["operator"] = "AND"
                queryDict["first"] = queryDict["content"].split(" AND ")[0]
                queryDict["second"] = queryDict["content"].split(" AND ")[1]
            elif " OR " in queryDict["content"]:
                queryDict["operator"] = "OR"
                queryDict["first"] = queryDict["content"].split(" OR ")[0]
                queryDict["second"] = queryDict["content"].split(" OR ")[1]
            elif " NOT " in queryDict["content"]:
                queryDict["operator"] = "NOT"
                queryDict["first"] = queryDict["content"].split(" NOT ")[1]
            elif ">" in queryDict["content"]:
                queryDict["operator"] = ">"
                queryDict["first"] = queryDict["content"].split(">")[1]
            elif "<" in queryDict["content"]:
                queryDict["operator"] = "<"
                queryDict["first"] = queryDict["content"].split("<")[1]
            else:
                queryDict["operator"] = "none"
        except Exception:
            return dict(error="You can not use any operators other than AND, OR, NOT, >, <")
        return queryDict


if __name__ == "__main__":
    lang = Query('book.review_count:"952"')
    result = lang.startParsing()
    print(result)
