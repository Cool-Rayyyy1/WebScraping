import React from "react";
import {useState} from 'react';
import {Button, Form, Input} from 'semantic-ui-react';

/**
 * This file defines the function of API for Getting the Information of a Author. 
 * User could call SearchAPI on this webpage and user need to enter the complex query about searching a author!
 * Otherwise, it will failed.
 * @returns Returns the information of the author searched based on the complex query
 */


function GetSearchAuthor () {
    /**
     * Two constant that has been defined.
     * query stores the complex query that the user entered in the frontEnd
     * item stores the information of the searching Author that returned by the API
    */
    const [query, setQuery] = useState("");
    const [item, setItem] = useState([]);
    return (
        <div>
            <Form>
                <Form.Field>
                    <Input
                        placeholder="Your Author query"
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
                        Get Author
                    </Button>
                </Form.Field>
                <Form.Field>
                    <li key={item[0]}>
                        AuthorId: {item[0]} | AuthorName: {item[1]} | AuthorUrl: {item[2]} | AuthorRating: {item[3]} 
                        | AuthorRatingCount: {item[4]} | AuthorReviewCount: {item[5]} | AuthorImageUrl: {item[6]} |
                        RelatedAuthors: {item[7]} | AuthorBooks: {item[8]}
                    </li>
                </Form.Field>
                
            </Form>
            
        </div>
    )
}

export default GetSearchAuthor