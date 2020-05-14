# Milestone Project 4 
## Andrea's Haberdashery Ecommerce App: Fullstack Frameworks Django Project
[![Build Status](https://travis-ci.com/callendera/MilestoneProject4.svg?branch=master)](https://travis-ci.com/callendera/MilestoneProject4)
## Check out App Deployed on Heroku [here](https://haberdashery-app.herokuapp.com/)
## Objective
Andrea's Haberdashery is a modern/minimalistic take on an old western travelor's inn. 
Our passion to provide holistic healing and comfort to our fellow weary travelors gives our website the edge 
in an ever developing world of health and self care.

My 4th and final Milestone Project is an Ecommerce Django Multi-App project. 
This project displays the knowledge I have gained throughout the course.
The skills learned in the modules leading up to this project including:
HTML Fundamentals, CSS Fundamentals, JavaScript, Interactive Frontend Developement, 
Python, Data Centric Developement, User Centric Development, and Django.
By adding Django to my skillset; I have developed an app that 
allows the user to make an account, reset password, add,edit,delete items in the cart, 
make purchases, and pull up order history. The app is a great way for our users to bask in self care, 
the excellent UX and Assesibility on a wide range of screensizes makes this app a a must for our users.
## Project Description and UX
The goal of this app is to provide a place where users can:
* Browse Products
* Register Account
* Log in/Sign out
* Add products to cart
* Edit/Update products in cart
* Delete products from cart
* Make purchases
* Look at order history
* View Product details
* Search for specific Products

The UX of the app was designed in a way to provide easy access and simplicity. 
The app is fully functional on all screen sizes with extensive testing for each feature on 1400px, 1200px, 992px, 768px, and 576px screensizes.

#### User Stories:
* As a user who would like to browse all products, upon landing on the home page and scrolling down, 
    all products are listed with the option to add to cart or to view details. 
    All products include an image, product name, shortened product dscription, and price. 
    If the user wants to veiw details while browsing products, when clicking the view details button a modal appears 
    that gives product image, name, a full description and price with an add to cart option or close option. 
    Specific categories of products are also available. If the user selects the shop herbal or shop succulents buttons on 
    second carousel slides, the user will be directed to those items on the home page.
* A user is looking for a speicfic product, they come to the landing page and select the search bar. 
    If they input a value that does not match
    any product in the database a message propmts them to search again. When a search is 
    input that matches items in the database, the screan is then automatically
    scrolled down to search results.
* User trying to make a purchase is propmted to sign in before continuing to check out 
    after adding items to their cart. when user is logged in, they are brought to the checkout once more so they can
    review order summary and then continue to the personal info form, all items are required besides Address 2. 
    Then, the card info is input. The submit button on the form 
    is accompanied by the review order button, this triggers a modal that pops up and asks if everything looks okay. 
    The modal is populated by items in the customers's cart and then 
    2 options; Update (takes user to cart to edit items), and Looks Good that closes the modal.
    When the user submits payment, a successful payment message appears and the user is take back to home page.
* User trying to login or create an account. On the home page, the user is shown a welcome message with some 
    info about Andrea's Haberdashery. There are also 2 buttons shown
    the 1st one prompts the user to Login, the 2nd asks user to register an account. If he user would like to login, 
    they can use the link in the Navbar to Login or follwo the button on the home page.
    The user is then met with a login page with a small form that asks for Username and Password. 
    If the user already has an account with Andrea's Haberdashery then, an error message will appear that gives
    the user will be logged in and taken to the home page that shows a successful login message.
    If the user would like to register an accunt they are taken to the register form by either using the Navbar or Register button on home page. 
    When the user registers they are tken to a Registration page that
    asks for email, username, and a password then password verificaton. 
    All fields are required and if the user is successfully registered, then a successful 
    registration message appears and takes the user to the profile page.
    Alternatively the user will Log Out by simply clicking the sign out button in Navbar.
* User who has made purchases and wants to see order history/details. AFter logging in, 
    the user can click on Profile symbol. The user then comes to the profile where their email and username are displayed, 
    then if the user has no order history a message shows under Order History Title that says the user has no order history and to go shop.
    If the user has order history, the history will appear in a list by date in a table. 
    Each order has a view details option that takes the user to another page that contains full item details, prices, and total cost of Order
* User making adjustments to cart. After adding items to their cart, the user can go to view their cart, 
    from there the user can remove items and edit the amount or each product. The remove product button shows up as a link
    and instantly removes item from cart. To edit, the user will use arrows to adjust the amount in input 
    field beside Qty and then click the "edit" icon, This automatically updates cart.

#### Wireframes:

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0001.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0002.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0003.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0004.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0005.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0006.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0007.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/dcb173682f0196e75a1b5870beda8ed9ba083b6c/static/images/wireframes/0008.jpg)

