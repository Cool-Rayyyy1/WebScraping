from src.API import queryParser
import mysql.connector
import json

# This file will simply test multiple complex query example to ensure that correct data will be found by the queryParser
if __name__ == "__main__":
    # first we print all the values in the database, which could help us to check
    conn = mysql.connector.connect(host='localhost', user='root', passwd='19990522', database='myquotes')
    c = conn.cursor(buffered=True)
    c.execute('''SELECT * FROM book''')
    columns = [col[0] for col in c.description]
    books = [dict(zip(columns, row)) for row in c.fetchall()]
    jsonBooks = json.dumps(books)
    print(jsonBooks)

    c.execute('''SELECT * FROM author''')
    columns = [col[0] for col in c.description]
    authors = [dict(zip(columns, row)) for row in c.fetchall()]
    jsonAuthors = json.dumps(authors)
    print(jsonAuthors)
    conn.commit()

    # Test begin
    # 1 we check the . field. An error should occur
    query1 = queryParser.Query('bookreview_count:"952"')
    result1 = query1.startParsing()
    assert result1 == dict(error="You need to specify . for the field")

    # 2 we check proper parameters. An error should occur
    query2 = queryParser.Query('people.review_count:"952"')
    result2 = query2.startParsing()
    assert result2 == dict(error="You must enter a book or a author")

    # 3 we check : sign. An error should occur
    query3 = queryParser.Query('book.review_count"952"')
    result3 = query3.startParsing()
    assert result3 == dict(error="You need to specify : for the field")

    # 4 we check findContent. First check proper ”“
    query4 = queryParser.Query('book.review_count:952"')
    result4 = query4.startParsing()
    assert result4 == dict(error="You need to have proper '' in your search!")

    # 5 we check findContent. First check proper ”“
    query5 = queryParser.Query('book.review_count:“952')
    result5 = query5.startParsing()
    assert result5 == dict(error="You need to have proper '' in your search!")

    # 6 check whether findContent could correctly find the book
    query6 = queryParser.Query('book.review_count:"952"')
    result6 = query6.startParsing()[0]
    assert result6[0] == "3735293"

    # 7 check whether findContent could correctly find the author
    query7 = queryParser.Query('author.rating:"4.2"')
    result7 = query7.startParsing()[0]
    assert result7[0] == "48622"

    # 8 Then we check the and operator for the author
    query8 = queryParser.Query('author.rating:4.34 AND rating_count:29178')
    result8 = query8.startParsing()[0]
    assert result8[0] == "45372"

    # 9 Then we check the and operator for the book
    query9 = queryParser.Query('book.ISBN:9780201616224 AND rating_count:16694')
    result9 = query9.startParsing()[0]
    assert result9[0] == "4099"

    # 10 Then we check the or operator for the author
    query10 = queryParser.Query('author.rating:4.34 OR rating_count:16734')
    result10 = []
    first10 = query10.startParsing()[0]
    second10 = query10.startParsing()[1]
    result10.append(first10[0])
    result10.append(second10[0])
    assert result10 == ['45372', '48622']

    # 11 Then we check the or operator for the book
    query11 = queryParser.Query('book.author:Andy Hunt OR rating_count:15980')
    result11 = []
    first11 = query11.startParsing()[0]
    second11 = query11.startParsing()[1]
    result11.append(first11[0])
    result11.append(second11[0])
    assert result11 == ['4099', '3735293']

    # Then we check the not function since the result is a little bit long, we just visually check it
    # 12 We first check not for the book. This should print all book except first one
    query12 = queryParser.Query('book.book_id: NOT 3735293')
    result12 = query12.startParsing()
    print(result12)

    # 13 We first check not for the author. This should print all author except first one
    query13 = queryParser.Query('author.name: NOT Michael C. Feathers')
    result13 = query13.startParsing()
    print(result13)

    # The rest 7 tests test the > and < for different situations first 4 books then 3 authors
    # 14 > sign for book
    query14 = queryParser.Query('book.ISBN:>9780201633609')
    result14 = query14.startParsing()[0]
    assert result14[0] == "85009"

    # 15 > sign for book
    query15 = queryParser.Query('book.rating:>4.30')
    result15 = []
    first15 = query15.startParsing()[0]
    second15 = query15.startParsing()[1]
    result15.append(first15[0])
    result15.append(second15[0])
    assert result15 == ['3735293', '4099']

    # 16 < sign for book. No book rating is less 4.0
    query16 = queryParser.Query('book.rating:<4.0')
    result16 = query16.startParsing()
    assert result16 == dict(error="No such item exist!")

    # 17 < sign for book
    query17 = queryParser.Query('book.book_id:<4100')
    result17 = query17.startParsing()[0]
    assert result17[0] == "4099"

    # 18 > sign for author
    query18 = queryParser.Query('author.review_count:>1900')
    result18 = query18.startParsing()[0]
    assert result18[0] == "45372"

    # 19 > sign for author. No author authorId > 1000000
    query19 = queryParser.Query('author.author_Id:>1000000')
    result19 = query19.startParsing()
    assert result19 == None


    # 20 < sign for author.
    query20 = queryParser.Query('author.rating:<4.13')
    result20 = []
    first20 = query20.startParsing()[0]
    second20 = query20.startParsing()[1]
    result20.append(first20[0])
    result20.append(second20[0])
    assert result20 == ['25201', '25215']

    print("Success! Passed 20/20 Tests!!!!!!!")

