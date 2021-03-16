import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';

/**
 * This file defines the function of achieving calling the POST API for the Author.
 * User could call post API on this webpage and user need to enter the information for creating such a brand new Author information
 * @returns Returns a message to tell the user that data has been created.
 */
function PostAuthor () {
    /**
     * Various constants to hold the text entered by the user!
    */
    const [id, setId] = useState("");
    const [name, setName] = useState("")
    const [authorUrl, setAuthorUrl] = useState("")
    const [rating, setRating] = useState("")
    const [ratingCount, setRatingCount] = useState("")
    const [reviewCount, setReviewCount] = useState("")
    const [imageUrl, setImageUrl] = useState("")
    const [relatedAuthors, setRelatedAuthors] = useState("")
    const [authorBooks, setAuthorBooks] = useState("")
    const [returnMessage, setMessage] = useState("")
    
    return (
        // First collecting the information for creating a bran-new Author
        <div>
            <Form>
                <Form.Field>
                    <Input
                        placeholder="Author Id"
                        value={id}
                        onChange={e => setId(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author Url"
                        value={authorUrl}
                        onChange={e => setAuthorUrl(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author Name"
                        value={name}
                        onChange={e => setName(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author Image Url"
                        value={imageUrl}
                        onChange={e => setImageUrl(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author related Authors"
                        value={relatedAuthors}
                        onChange={e => setRelatedAuthors(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author books"
                        value={authorBooks}
                        onChange={e => setAuthorBooks(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author Rating"
                        value={rating}
                        onChange={e => setRating(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author Rating Count"
                        value={ratingCount}
                        onChange={e => setRatingCount(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Author Review Count"
                        value={reviewCount}
                        onChange={e => setReviewCount(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Button onClick={ async () => {
                        // creating a dic values which are used later when calling the API
                        const author = {"author_Id":id, "name":name, "author_url":authorUrl, "rating":rating, "rating_count":ratingCount, "review_count":reviewCount, "image_url":imageUrl, "related_author":relatedAuthors, "author_books":authorBooks}
                        fetch('/api/author', {
                            method: "POST", 
                            headers:{
                                'Content-Type':'application/json'
                            },
                            body: JSON.stringify(author)}).then(() => setMessage("Author has been added!"))
                    }
                    }>
                        Post Author
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

export default PostAuthor