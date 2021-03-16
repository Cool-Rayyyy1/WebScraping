/*
The code below are the packages and the diffrent components under the Pages folder
*/

import React, { Component } from "react";
import {
  BrowserRouter as Router, 
  Route,
  Switch,
  Redirect
} from "react-router-dom";

import MainPage from "./Pages";
import NotFoundPage from "./Pages/404";
import GetAllBooks from "./Pages/getBooksAll";
import PutBook from "./Pages/putBook";
import GetBook from "./Pages/getBook";
import GetAllAuthor from "./Pages/getAuthorAll";
import GetAuthor from "./Pages/getAuthor";
import GetSearchBook from "./Pages/getSearchBook";
import DeleteBook from "./Pages/deleteBook";
import DeleteAuthor from "./Pages/deleteAuthor";
import PutAuthor from "./Pages/putAuthor";
import PostBook from "./Pages/postBook";
import PostAuthor from "./Pages/postAuthor";
import GetSearchAuthor from "./Pages/getSearchAuthor";

/**
 * Class App defines the routes for all kinds of websites.
 * App will check each Routes by order and if none of routes has been found, it will redirect to 404 page!
 */
class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
        <Route exact path ="/" component={MainPage} />
        <Route exact path = "/404" component={NotFoundPage} />
        <Route exact path = "/getBookAll" component={GetAllBooks}/>
        <Route exact path = "/getBook" component={GetBook}/>
        <Route exact path = "/getAuthorAll" component={GetAllAuthor}/>
        <Route exact path = "/getAuthor" component={GetAuthor}/>
        <Route exact path = "/getSearchBook" component={GetSearchBook}/>
        <Route exact path = "/getSearchAuthor" component={GetSearchAuthor}/>
        <Route exact path = "/putBook" component={PutBook}/>
        <Route exact path = "/putAuthor" component={PutAuthor}/>
        <Route exact path = "/postBook" component={PostBook}/>
        <Route exact path = "/postAuthor" component={PostAuthor}/>
        <Route exact path = "/deleteBook" component={DeleteBook}/>
        <Route exacy path = "/deleteAuthor" component={DeleteAuthor}/>
        <Redirect to="/404"/>
        </Switch>
       </Router>
    ) 
  }
}

export default App;