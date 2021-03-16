# sp21-cs242-assignment2.2
Due date: :crescent_moon: 23:59 CDT March 15, 2021 :clock12: <br>

### Part I: Render and update content
:round_pushpin:<br>
There are a couple of approaches to render content. For example, you can use a template engine like jinja to render everything at backend, or you can develop a single-page application using frameworks like React or Angular to render everything at frontend. To better prepare for future assignments, we will adopt a frontend-heavy approach. You are required to use JavaScript to make requests to all of the APIs we developed last week and render corresponding content on webpage, and all else (including routing, if you need) can be done either in server or in browser. At a minimum, your server will need to serve at least one html (hint) as the starting point of your website. From that point on, you are welcome to either develop and serve more HTMLs and making requests in script, or perform all operations on a single HTML page.<br>

To make requests in browser, we recommend you using either fetch or axios. To render contents, you can either use native DOM api, libraries like jQuery and React, or frameworks like Angular. If you are new to frontend development, we suggest you start from the native DOM api to get a better understanding of how browsers present content on screen.<br>

Note that you must render API results instead of leaving JSON strings on webpage.<br>

### Part2 API Creation
:round_pushpin:<br>
If you haven't developed the wild card operator for query string from last week's assignment, you may need to add more APIs to your server that get all books and authors from the database. In this part, you'll need to create visualizations on webpage using d3.js and svg elements only.

What your program should support:

* Visualize the ranking of top k highest rated authors.
   * The number k should be adjustable, and the visualization should update accordingly. You must allow users to adjust k dynamically by inputing numbers in the UI.
   * This visualization should be in a separate route "/vis/top-authors". If you use routing at backend, this means that it will likely be in a separate HTML page. If you use a frontend framework, this means that you need to configure routes in browser.
* Visualize the ranking of top k highest rated books.
   *  The number k should be adjustable, and the visualization should update accordingly. You must allow users to adjust k dynamically by inputing numbers in the UI.
   *  This visualization should be in a separate route "/vis/top-books"

