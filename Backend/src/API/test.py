
import json
import flask
import mysql.connector
from flask import request, jsonify, Response

conn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
c = conn.cursor(buffered=True)

def takeSecond(elem):
    return elem[1]


def test(inputK):

    if inputK is None:
        return "Error: No id field provided. Please specify an id."
    try:
        sql = "SELECT book_id, rating FROM Book"
        c.execute(sql)
        conn.commit()
        tempList = c.fetchall()
        nonSortList = []
        for data in tempList:
            nonSortList.append((data[0], float(data[1])))
        sortList = sorted(nonSortList, key=takeSecond, reverse=True)
        finalList = []
        for i in range(int(inputK)):
            finalList.append(sortList[i])
        returnList = []
        for each in finalList:
            searchSql = "SELECT * FROM Book WHERE book_id = %s"
            target = (each[0],)
            c.execute(searchSql, target)
            searchResult = c.fetchall()
            returnList.append(searchResult)
        return returnList
    except Exception as e:
        return e

if __name__ == '__main__':
    result = test(2)
    print(result)
