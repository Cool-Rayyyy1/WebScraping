import React from "react";

/**
 * This file defines the class of API for Getting the Information of all Authors. 
 * User could call get all Authors API on this webpage.
 * @returns Returns parts of the information of all the authors
 */

class GetAllAuthor extends React.Component {
    /**
     * Two constant that has been defined.
     * IsLoaded defineds whether the data has been loaded.
     * item stores the information of the searching Author that returned by the API
    */
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded:false,
        }
    } 

    componentDidMount() {
        // Call the Api and initializes the consructor props.
        fetch('/api/authors/all')
            .then(res => res.json())
            .then(json => {
                this.setState({
                    isLoaded: true,
                    items: json,
                })
            })
    }
    
    render() {
        var { isLoaded, items } = this.state;
        if (!isLoaded) {
            return <div>Loading...</div>;
        }
        else {
            return (
                <div className="App">
                    <ul>
                        {items.map(item => (
                            <li key={item.author_Id}>
                                AuthorId: {item.author_Id} | Name: {item.name} | Author_Url: {item.author_url} | Rating: {item.rating} | AuthorRaingCount: {item.rating_count}
                            </li>
                        ))}
                    </ul>

                </div>
            )
        }
    
    }
}

export default GetAllAuthor