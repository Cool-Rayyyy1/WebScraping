import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';

/**
 * This file defines the function of API for Deleting a Book. 
 * User could call deleteBook API on this webpage.
 * @returns Returns a message to tell user that whether the Book has been deleted.
 */

function DeleteBook () {
    /**
     * Two constant that has been defined.
     * id stores the id that the user want to delete
     * item stores the message information that returned by the API
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
                        //call the API
                        await fetch('/api/book?id=' + id, {
                            method: "DELETE"
                        }).then(response => response.json())
                            .then(data => {
                                console.log(data)
                                let data_array = []
                                data_array.push(data)
                                setBook(data_array)
                            })
                    }}>
                        Delete Book
                    </Button>
                </Form.Field>
                <Form.Field>
                    {item.map(item => (
                        // show the message returned by the API
                        <li key={item.message}>
                            status: {item.message}
                        </li>
                    ))}
                </Form.Field>
                
            </Form>
               
        </div>
    )
}

export default DeleteBook