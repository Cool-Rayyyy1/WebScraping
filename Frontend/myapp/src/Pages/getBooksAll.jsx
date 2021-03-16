import React from "react";


/**
 * This file defines the class of API for Getting the Information of all Books. 
 * User could call get all Books API on this webpage.
 * @returns Returns parts of the information of all the books
 */


class GetAllBooks extends React.Component {
    /**
     * Two constant that has been defined.
     * IsLoaded defineds whether the data has been loaded.
     * item stores the information of the searching Book that returned by the API
    */
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded:false,
        }
    } 

    componentDidMount() {
        // call the API and initializes the values of the constructor props
        fetch('/api/books/all')
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
            // if calling API failed, Loading will be shown
            return <div>Loading...</div>;
        }
        else {
            // Otherwise, show parts of the information of the books
            return (
                <div className="App">
                    <ol>
                        {items.map(item => (
                            <li key={item.book_id}>
                                BookId: {item.book_id} | BookName: {item.title} | ISBN: {item.ISBN} | BookAuthor: {item.author} | BookRating: {item.rating}

                            </li>
                         ))}
                    </ol>
                </div>
            )
        }
    
    }
}

export default GetAllBooks