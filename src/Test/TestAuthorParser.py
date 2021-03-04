from src.WebScraper import AuthorParser

# This file tests whether the AuthorParse correctly handles scraping data
if __name__ == '__main__':
    # Check first great author page
    firstAuthor = AuthorParser.Author("https://www.goodreads.com/author/show/45372.Robert_C_Martin")
    firstName = firstAuthor.getName()
    assert firstName == "Robert C. Martin"
    firstUrl = firstAuthor.getAuthorUrl()
    assert firstUrl == "https://www.goodreads.com/author/show/45372.Robert_C_Martin"
    firstId = firstAuthor.getAuthorId()
    assert firstId == str(45372)
    firstRating = firstAuthor.getRating()
    assert firstRating == str(4.34)
    firstRatingCount = firstAuthor.getRatingCount()
    assert firstRatingCount == str(29097)
    firstReviewCount = firstAuthor.getReviewCount()
    assert firstReviewCount == str(1915)
    firstImageUrl = firstAuthor.getImageUrl()
    assert firstImageUrl == "https://www.goodreads.com/photo/author/45372.Robert_C_Martin"
    firstRelatedAuthors = firstAuthor.getRelatedAuthors()
    relatedAuthorList = ['Andy Hunt', 'Steve McConnell', 'Michael C. Feathers', 'Kent Beck', 'Martin Fowler', 'Eric Freeman', 'Erich Gamma', 'Joshua Bloch', 'Eric Evans', 'Sam Newman', 'Steve  Freeman']
    assert firstRelatedAuthors == relatedAuthorList
    firstAuthorBook = firstAuthor.getAuthorsBooks()
    authorBookList = ['Clean Code: A Handbook of Agile Software Craftsmanship', 'The Clean Coder: A Code of Conduct for Professional Programmers', 'Clean Architecture', 'Agile Software Development, Principles, Patterns, and Practices', 'Agile Principles, Patterns, and Practices in C#', 'Clean Agile: Back to Basics', 'The Robert C. Martin Clean Code Collection', 'UML for Java Programmers', 'Pattern Languages of Program Design 3', 'Design Principles and  Design Patterns']
    assert firstAuthorBook == authorBookList

    # Check second unnormal author page
    secondAuthor = AuthorParser.Author("https://www.goodreads.com/author/show/81619.Daniel_J_Levitin")
    secondName = secondAuthor.getName()
    assert secondName == "Daniel J. Levitin"
    secondUrl = secondAuthor.getAuthorUrl()
    assert secondUrl == "https://www.goodreads.com/author/show/81619.Daniel_J_Levitin"
    secondId = secondAuthor.getAuthorId()
    assert secondId == str(81619)
    secondRating = secondAuthor.getRating()
    assert secondRating == str(3.83)
    secondRatingCount = secondAuthor.getRatingCount()
    assert secondRatingCount == str(72962)
    secondReviewCount = secondAuthor.getReviewCount()
    assert secondReviewCount == str(3701)

    secondRelatedAuthors = secondAuthor.getRelatedAuthors()
    relatedAuthorList = ['Richard Dawkins', 'Steven Johnson', 'Jeffrey M. Schwartz', 'Steven Pinker', 'Stephen Booth', 'V.S. Ramachandran', 'Philip Toshio Sudo', 'David Byrne', 'Aaron Copland', 'Leonard Bernstein', 'John Cage', 'Barry Green', 'J. Peter Burkholder', 'Patti Smith', 'Linda Moore', 'Joseph E. LeDoux', 'Jonah Lehrer', 'Oliver Sacks', 'Sharon J. Bolton', 'Alex  Ross', 'Julie Klausner', 'Victor L. Wooten', 'Rachel Hollis', 'John        Powell', 'Mark  Levine']
    # check relatedAuthorList visually
    secondAuthorBook = secondAuthor.getAuthorsBooks()
    authorBookList = ['This Is Your Brain on Music: The Science of a Human Obsession', 'The Organized Mind: Thinking Straight in the Age of Information Overload', 'The World in Six Songs', 'A Field Guide to Lies: Critical Thinking in the Information Age', 'Successful Aging: A Neuroscientist Explores the Power and Potential of Our Lives', 'Foundations of Cognitive Psychology: Core Readings', 'From Demo Tape to Record Deal: Handy Guide', 'The Organized Mind, The Power of Habit, Thinking Fast and Slow 3 Books Collection Set', 'The World in Six Songs: How the Musical Brain Created Human Nature', 'Weaponized Lies: How to Think Critically in the Post-Truth Era by Daniel J. Levitin, Dutton']
    # check authorBookList visually
    secondImageUrl = secondAuthor.getImageUrl()
    # unnormal image assert secondImageUrl == "https://s.gr-assets.com/assets/nophoto/user/u_200x266-e183445fd1a1b5cc7075bb1cf7043306.png"

