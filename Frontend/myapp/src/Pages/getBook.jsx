import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';

/**
 * This file defines the function of API for Getting the Information of a Book. 
 * User could call getBook API on this webpage.
 * @returns Returns all the information of the Book that the user want to search
 */


function GetBook () {
    /**
     * Two constant that has been defined.
     * id stores the id that the user want to get
     * item stores the information of the searching Book that returned by the API
    */
    const [id, setId] = useState("");
    const [item, setBook] = useState([]);
    return (
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
                    <Button onClick={ async () => {
                        let data_array = []
                        // call the API
                        fetch('/api/book?id=' + id).then(response =>
                            response.json()).then(data => {
                                console.log(data)
                                if (data === undefined) {
                                    data_array.push(data)
                                } else {
                                    for (let i = 0; i < data.length; i++) {
                                        data_array.push(data[i]);
                                    }
                                }
                        }).then(() => setBook(data_array))
                    }
                    }>
                        Get Book
                    </Button>
                    <ol>
                        {item.map(item => (
                            // show the information of the book
                            <li key={item.book_id}>
                                BookId: {item.book_id} | BookName: {item.title} | ISBN: {item.ISBN} | BookAuthor: {item.author} | BookRating: {item.rating}
                            </li>
                        ))}
                    </ol>
                </Form.Field>
            </Form>
            
        </div>
    )
}

export default GetBook