import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';


/**
 * This file defines the function of API for Getting the Information of a Author. 
 * User could call getAuthor API on this webpage.
 * @returns Returns all the information of the Author
 */

function GetAuthor () {
    /**
     * Two constant that has been defined.
     * id stores the id that the user want to get
     * item stores the information of the searching Author that returned by the API
    */
    const [id, setId] = useState("");
    const [item, setAuthor] = useState([]);
    return (
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
                    <Button onClick={ async () => {
                        let data_array = []
                        //call the api
                        fetch('/api/author?id=' + id).then(response =>
                            response.json()).then(data => {
                                console.log(data)
                                if (data === undefined) {
                                    data_array.push(data)
                                } else {
                                    for (let i = 0; i < data.length; i++) {
                                        data_array.push(data[i]);
                                    }
                                }
                        }).then(() => setAuthor(data_array))
                    }
                    }>
                        Get Author
                    </Button>
                </Form.Field>
                <Form.Field>
                    {item.map(item => (
                        // show the author information
                        <li key={item.author_Id}>
                             AuthorId: {item.author_Id} | Name: {item.name} | Author_Url: {item.author_url} | Rating: {item.rating} | AuthorRaingCount: {item.rating_count}
                        </li>
                    ))}
                </Form.Field>
                   
            </Form>
            
        </div>
    )
}

export default GetAuthor