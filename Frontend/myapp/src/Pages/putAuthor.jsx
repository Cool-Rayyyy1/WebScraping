import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';

/**
 * This file contains the function for updating the information of the author.
 * User could call the PUT API for the author on this webpage and user need to enter the variable that they want to change
 * @returns Returns a message to tell the user whether the database has been updates.
 */

function PutAuthor () {
     /**
     * Four constant that has been defined.
     * id stores the id of the Author that the user want to update
     * upFiled store the field that the user want to update
     * upValue store the value that the user want to update for that field
     * returnMessage will tell the user whether the Author has been updated
    */
    const [id, setId] = useState("");
    const [upFiled, setField] = useState("")
    const [upValue, setUpValue] = useState("")
    const [returnMessage, setMessage] = useState("")
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
                    <Input
                        placeholder="Author Field"
                        value={upFiled}
                        onChange={e => setField(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Input
                        placeholder="Update value"
                        value={upValue}
                        onChange={e => setUpValue(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Button onClick={ async () => {
                        var formData = new FormData()
                        formData.append(upFiled,upValue)
                        fetch('/api/author?id=' + id, {
                            method: "PUT", 
                            body: formData}).then(() => setMessage("Author has already been updated!"))
                    }
                    }>
                        Update Author
                    </Button>
                    
                </Form.Field>
                <Form.Field>
                    <li>
                        status: {returnMessage}
                    </li>
                </Form.Field>
                
            </Form>
            
        </div>
    )
}

export default PutAuthor