import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';

/**
 * This file defines the function of API for Getting the Information of a Book. 
 * User could call SearchAPI on this webpage and user need to enter the complex query about searching a book!
 * Otherwise, it will failed.
 * @returns Returns the information of the book searched based on the complex query
 */


function GetSearchBook () {
    /**
     * Two constant that has been defined.
     * query stores the complex query that the user entered in the frontEnd
     * item stores the information of the searching Book that returned by the API
    */
    const [query, setQuery] = useState("");
    const [item, setItem] = useState([]);
    return (
        <div>
            <Form>
                <Form.Field>
                    <Input
                        placeholder="Your Book query"
                        value={query}
                        onChange={e => setQuery(e.target.value)}
                    />
                </Form.Field>
                <Form.Field>
                    <Button onClick={ async () => {
                        let data_array = []
                        // call the API
                        fetch('/api/search?q=' + query).then(response =>
                            response.json()).then(data => {
                                let dataList = data[0]
                                for (let i = 0; i <dataList.length; i++) {
                                    data_array.push(dataList[i]);
                                }
                                console.log(typeof(dataList))
                        }).then(() => setItem(data_array))
                    }
                    }>
                        Get Book
                    </Button>
                </Form.Field>
                <Form.Field>
                    <li key={item[0]}>
                        BookId: {item[0]} | BookUrl: {item[1]} | BookName: {item[2]} | ISBN: {item[3]} | BookAuthorUrl: {item[4]} |
                        BookAuthor: {item[5]} | BookRating: {item[6]} | BookRatingCount: {item[7]} | BookReviewCount: {item[8]} | BookImage: {item[9]} |
                        RelatedBooks: {item[10]}
                    </li>
                </Form.Field>
                    
            </Form>
            
        </div>
    )
}

export default GetSearchBook