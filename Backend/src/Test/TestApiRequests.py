import mysql.connector
import json

# Because ApiRequests are hard to test by unit tests. This file will first display all the data in the current database and then documents how to test API

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
    # Now we have all the data which could help us to do the postman checks
    # First open the postman app, and go to the workspace page and enter the url

    ## For get method, simply just enter the required methods

    ## For put method, except enter the required values in the params place, write some required parameters in the forma data palce

    ## For post method, below are some test data, which could be directly inserted in the raw data place.
    # single book
    var1 = {
        "book_id": "3735293",
        "book_url": "https://www.goodreads.com/book/show/3735293-clean-code?from_search=true&qid=HhMDV0vMa5&rank=1",
        "title": "Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin",
        "ISBN": "9780132350884",
        "author_url": "https://www.goodreads.com/author/show/45372.Robert_C_Martin",
        "author": "Robert C. Martin",
        "rating": " 4.40 ",
        "rating_count": "15973",
        "review_count": "950",
        "image_url": "https://www.goodreads.com/book/photo/3735293-clean-code",
        "similar_books": ["The Pragmatic Programmer: From Journeyman to Master",
                          "Design Patterns: Elements of Reusable Object-Oriented Software",
                          "Refactoring: Improving the Design of Existing Code", "Head First Design Patterns",
                          "Code Complete", "Effective Java", "Test-Driven Development: By Example",
                          "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                          "Working Effectively with Legacy Code", "Designing Data-Intensive Applications",
                          "The Software Craftsman: Professionalism, Pragmatism, Pride",
                          "The Mythical Man-Month: Essays on Software Engineering",
                          "Building Microservices: Designing Fine-Grained Systems",
                          "Growing Object-Oriented Software, Guided by Tests", "Java Concurrency in Practice",
                          "JavaScript: The Good Parts", "Patterns of Enterprise Application Architecture",
                          "Extreme Programming Explained: Embrace Change (The XP Series)",
                          "Implementing Domain-Driven Design",
                          "Cracking the Coding Interview: 150 Programming Questions and Solutions",
                          "Grokking Algorithms An Illustrated Guide For Programmers and Other Curious People",
                          "Introduction to Algorithms", "Head First Java",
                          "Eloquent JavaScript: A Modern Introduction to Programming", "C# in Depth",
                          "The Art of Unit Testing: With Examples in .NET", "The C Programming Language",
                          "Soft Skills: The Software Developer's Life Manual",
                          "Release It!: Design and Deploy Production-Ready Software (Pragmatic Programmers)",
                          "Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions"]
    }

    # book list
    var2 = [
        {
            "book_id": "3735293",
            "book_url": "https://www.goodreads.com/book/show/3735293-clean-code?from_search=true&qid=HhMDV0vMa5&rank=1",
            "title": "Clean Code: A Handbook of Agile Software Craftsmanship by Robert C. Martin",
            "ISBN": "9780132350884",
            "author_url": "https://www.goodreads.com/author/show/45372.Robert_C_Martin",
            "author": "Robert C. Martin",
            "rating": " 4.40 ",
            "rating_count": "15973",
            "review_count": "950",
            "image_url": "https://www.goodreads.com/book/photo/3735293-clean-code",
            "similar_books": ["The Pragmatic Programmer: From Journeyman to Master",
                              "Design Patterns: Elements of Reusable Object-Oriented Software",
                              "Refactoring: Improving the Design of Existing Code", "Head First Design Patterns",
                              "Code Complete", "Effective Java", "Test-Driven Development: By Example",
                              "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                              "Working Effectively with Legacy Code", "Designing Data-Intensive Applications",
                              "The Software Craftsman: Professionalism, Pragmatism, Pride",
                              "The Mythical Man-Month: Essays on Software Engineering",
                              "Building Microservices: Designing Fine-Grained Systems",
                              "Growing Object-Oriented Software, Guided by Tests", "Java Concurrency in Practice",
                              "JavaScript: The Good Parts", "Patterns of Enterprise Application Architecture",
                              "Extreme Programming Explained: Embrace Change (The XP Series)",
                              "Implementing Domain-Driven Design",
                              "Cracking the Coding Interview: 150 Programming Questions and Solutions",
                              "Grokking Algorithms An Illustrated Guide For Programmers and Other Curious People",
                              "Introduction to Algorithms", "Head First Java",
                              "Eloquent JavaScript: A Modern Introduction to Programming", "C# in Depth",
                              "The Art of Unit Testing: With Examples in .NET", "The C Programming Language",
                              "Soft Skills: The Software Developer's Life Manual",
                              "Release It!: Design and Deploy Production-Ready Software (Pragmatic Programmers)",
                              "Enterprise Integration Patterns: Designing, Building, and Deploying Messaging Solutions"]
        },
        {
            "book_id": "4099",
            "book_url": "https://www.goodreads.com/book/show/4099.The_Pragmatic_Programmer",
            "title": "The Pragmatic Programmer: From Journeyman to Master by Andy Hunt",
            "ISBN": "9780201616224",
            "author_url": "https://www.goodreads.com/author/show/2815.Andy_Hunt",
            "author": "Andy Hunt",
            "rating": " 4.32 ",
            "rating_count": "16689",
            "review_count": "979",
            "image_url": "https://www.goodreads.com/book/photo/4099.The_Pragmatic_Programmer",
            "similar_books": ["Clean Code: A Handbook of Agile Software Craftsmanship",
                              "Design Patterns: Elements of Reusable Object-Oriented Software",
                              "Refactoring: Improving the Design of Existing Code", "Code Complete",
                              "The Mythical Man-Month: Essays on Software Engineering",
                              "The Clean Coder: A Code of Conduct for Professional Programmers",
                              "Head First Design Patterns", "Clean Architecture",
                              "Working Effectively with Legacy Code",
                              "Extreme Programming Explained: Embrace Change (The XP Series)",
                              "JavaScript: The Good Parts", "Test-Driven Development: By Example", "Effective Java",
                              "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                              "Soft Skills: The Software Developer's Life Manual",
                              "Designing Data-Intensive Applications", "The Passionate Programmer",
                              "Structure and Interpretation of Computer Programs (MIT Electrical Engineering and Computer Science)",
                              "Building Microservices: Designing Fine-Grained Systems",
                              "Peopleware: Productive Projects and Teams", "The C Programming Language",
                              "Fundamentals of Software Architecture: An Engineering Approach",
                              "Patterns of Enterprise Application Architecture",
                              "Coders at Work: Reflections on the Craft of Programming",
                              "Release It!: Design and Deploy Production-Ready Software (Pragmatic Programmers)",
                              "Effective C++: 55 Specific Ways to Improve Your Programs and Designs",
                              "The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business Win",
                              "Clean Agile: Back to Basics", "Introduction to Algorithms",
                              "Code: The Hidden Language of Computer Hardware and Software"]
        }
    ]

    ## For delete method, simple enter the required parameters for which book or author that need to be deleted.
