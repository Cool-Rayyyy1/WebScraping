import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';

/**
 * This file defines the function of achieving calling the POST API for the Book.
 * User could call post API on this webpage and user need to enter the information for creating such a brand new Book information
 * @returns Returns a message to tell the user that data has been created.
 */

function PostBook () {
    /**
     * Various constants to hold the text entered by the user!
    */
    const [id, setId] = useState("");
    const [url, setUrl] = useState("")
    const [title, setTitle] = useState("")
    const [ISBN, setISBN] = useState("")
    const [authorUrl, setAuthorUrl] = useState("")
    const [author, setAuthor] = useState("")
    const [rating, setRating] = useState("")
    const [ratingCount, setRatingCount] = useState("")
    const [reviewCount, setReviewCount] = useState("")
    const [imageUrl, setImageUrl] = useState("")
    const [similarBooks, setSimilarBooks] = useState("")
    const [returnMessage, setMessage] = useState("")

    return (
        // First collecting the information for creating a bran-new Book
        <div>
            <Form>
                <Form.Field>
                    <Input
                        placeholder="Book Id"
                        value={id}
                        onChange={e => setId(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book Url"
                        value={url}
                        onChange={e => setUrl(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book ISBN"
                        value={ISBN}
                        onChange={e => setISBN(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book title"
                        value={title}
                        onChange={e => setTitle(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book authorUrl"
                        value={authorUrl}
                        onChange={e => setAuthorUrl(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book Author"
                        value={author}
                        onChange={e => setAuthor(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book Rating"
                        value={rating}
                        onChange={e => setRating(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book Rating Count"
                        value={ratingCount}
                        onChange={e => setRatingCount(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book reviewCount"
                        value={reviewCount}
                        onChange={e => setReviewCount(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book Image Url"
                        value={imageUrl}
                        onChange={e => setImageUrl(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Book similar Books"
                        value={similarBooks}
                        onChange={e => setSimilarBooks(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Button onClick={ async () => {
                        // creating a dic values which are used later when calling the API
                        const book = {"book_id":id, "book_url":url, "title":title, "ISBN":ISBN, "author_url":authorUrl, "author":author, "rating":rating, "rating_count":ratingCount, "review_count":reviewCount, "image_url":imageUrl, "similar_books":similarBooks}
                        await fetch('/api/book', {
                            method: "POST", 
                            headers:{
                                'Content-Type':'application/json'
                            },
                            body: JSON.stringify(book)}).then(() => setMessage("Book has already been created!"))
                    }
                    }>
                        Post Book
                    </Button>
                    
                </Form.Field>
                <Form.Field>
                    <li>
                        status:{returnMessage}
                    </li>
                </Form.Field>
                
            </Form>
            
        </div>
    )
}

export default PostBook