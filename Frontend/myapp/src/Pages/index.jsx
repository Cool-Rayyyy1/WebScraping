import React from "react";
import { Link } from "react-router-dom";

/**
 * The const MainPage defines the links to different APIs.
 * User could click different links to get into the webpage.
 */

const MainPage = () => {
    return (
        <div>
            <h1>Welcome to Api main page</h1>
            <p><Link to="/getBookAll">GetBookAll</Link></p>
            <p><Link to="/getBook">GetBook</Link></p>
            <p><Link to="/getAuthorAll">GetAuthorAll</Link></p>
            <p><Link to="/getAuthor">GetAuthor</Link></p>
            <p><Link to="/getSearchBook">GetSearchBook</Link></p>
            <p><Link to="/getSearchAuthor">GetSearchAuthor</Link></p>
            <p><Link to="/putBook">PutBook</Link></p>
            <p><Link to="/putAuthor">PutAuthor</Link></p>
            <p><Link to="/postBook">PostBook</Link></p>
            <p><Link to="/postAuthor">PostAuthor</Link></p>
            <p><Link to="/deleteBook">DeleteBook</Link></p>
            <p><Link to="/deleteAuthor">DeleteAuthor</Link></p>
        </div>
    
    )
}

export default MainPage