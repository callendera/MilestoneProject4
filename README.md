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

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/119a0b187c58ed39c285fc444ca90d894827d06f/static/images/wireframes/0001.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/9678331417588b80e9ccedb9ec96cc3ffe2405a6/static/images/wireframes/0002.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/9678331417588b80e9ccedb9ec96cc3ffe2405a6/static/images/wireframes/0003.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/9678331417588b80e9ccedb9ec96cc3ffe2405a6/static/images/wireframes/0004.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/9678331417588b80e9ccedb9ec96cc3ffe2405a6/static/images/wireframes/0005.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/9678331417588b80e9ccedb9ec96cc3ffe2405a6/static/images/wireframes/0006.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/9678331417588b80e9ccedb9ec96cc3ffe2405a6/static/images/wireframes/0007.jpg)

![WireFrame](https://github.com/callendera/MilestoneProject4/blob/9678331417588b80e9ccedb9ec96cc3ffe2405a6/static/images/wireframes/0008.jpg)

## Features

### Existing Features
* Navbar 
    * Fixed to the top for easy navigation 
    * Andrea's Haberdashery Logo in center
    * Includes: Home|Sign in|Create Account|Cart Each navigates you throughout the app
    * Search bar also in Navbar, searches product database
    * Navigation links become a toggler in the mobile veiw and smaller screen sizes
* Carousel
    * First slide
        * If user is not logged in: it gives a welcome message and login or register buttons
        * If user is logged in: the welcome message chnanges to Hey There and directs the user to brows the products below
    * Second slide 
        * This slide gives the user 2 Categories to shop in
        * Shop Herbal and Shop Succulents runs a search and displays the products that match either search
    * Third slide   
        * Tells user about Free Shipping
* List of all Products
    * Avaliable when the user navigates to the Home page using the navbar. Displays all products present in the database. 
    * Each Product has the option to view details or Add to cart 
* Modal #1
    * Shows full Product details and description
    * Option to Add item to cart or close modal.
* Profile
    * User profile displays username, email, Order history list in a table
    * Order History 
        * This feature is reached through the profile, and is shown in a table the initial look in the profile shows the lists by date and total
        * The option to view Order Details displays new page that includes product images, quantities, and order total
* Login/Registration
    * In the Navbar the user is given the options to login or register, options also given in 1st slide of Carousel
    * For both the user is directed to new pages with either login or registration form feilds, all are required. 
    * Sign Out  
        * To sign out, use the navbar link for signing out. 
* Cart 
    * When adding items to the cart the cart option in the Navbar has a badge that displays item amount in the cart
    * The cart itself is displayed with cart items in individual rows that seperate with a block divider
    * The products displayed all show product image, product name, short product description, price, Quantity
    * The items in the cart also have options to remove or edit Qty in the cart. 
    * At the bottom of the cart the total is shown and the checkout button directs the user to pay.
* Checkout
    * After viewing the cart, the checkout presents an Order History with Order total.
    * below order summary there is a link to go back to cart.
    * Forms are displayed for personal info for shipping and Card payment info 
    * At the bottom there are options to submit payment or review order. 
    * Modal #2 This modal asks if the order looks right, it gives user option to update cart or that it all looks Good
        * If the Update button is clicked, the user is redirected back to cart to make edits.
    * When the order is completed the user is redirected to Home Page with Successfully paid message. That order is then available in the order hitory

### Features left to Implement 
* Reset Password    
    * I will also include in Bugs, I never got the errors for Reset Password resolved.
    * Right now the reset password email only shows as sent for some gmail accounts no yahoo or outlook accounts and wont send actual email.
* Shipping tracker
    * Was apart of my original plans, but I ran out of time 
* Product Reviews
    * Was apart of my original plans, but I ran out of time 
* Edit User Info in Profile
    * Was apart of my original plans, but I ran out of time 

## Tools/Technologies
* [GitPod](https://www.gitpod.io/)
    * GitPodw hosted my Workspace for this project
* [Git](https://git-scm.com/)
    * used to push and commit any and all changes to my repository on GitHub
* [Bootstrap](https://getbootstrap.com/)
    * Installed as a dependency Provided my buttons, modals, Navbar, footer, table and basic grid structure. 
    * Also used django-bootstrap-forms
* [JQuery](https://jquery.com/)
    * The project uses JQuery for DOM manipulation (Ex: Modal)
* [JavaScript](https://www.javascript.com/)
    * Used along with Bootstrap for the modal, Stripe Payments
* [SQLite](https://www.sqlite.org/index.html)
    * used as my local database until I engaged Database Url for Postgres
* [Heroku](https://signup.heroku.com/t/platform?c=70130000001xDpdAAE&gclid=EAIaIQobChMI_ZvP4LXl5QIVEYzICh1T0g2FEAAYASAAEgIoQPD_BwE)
    * Deployment of my app Andrea's Haberdashery
* [Postgres](https://www.postgresql.org/docs/9.2/install-procedure.html)
    * Database used in Heroku after deployment
* [S3 Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
    * Stored all static files: CSS, JS, and Images
* [Travis CI](https://travis-ci.org/)
    * Runs continuous automated tests

## Testing
### Automated Testing
* Validation Services
    * [W3C Markup Validator](https://validator.w3.org/) was used to validate my HTML code.
    * [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate my CSS code.
    * [JSHint](https://jshint.com/) was used to test JS code.
    * [Travis CI](https://travis-ci.org/) Runs constant testing.

### UX Stories: Testing / Manual Testing
All features were tested on Google Chrome, Internet Explorer, and Firefox. Mobile/Tablet features were tested on Apple and Samsung devices. Everything was tested using a wide range of screensizes.
* Accounts App - As a user I want to:
    * Login:
        * After coming to the home page,
        * I can either use the Navbar login link or the Login option in Slide 1 of the Carousel
        * After clicking the login button, I am directed to the login page that is triggered by the Login view in the accounts app
        * The form is all required and if the user has an account then they will be logged in and redirected to the home page.
        * If the user does not already have an account and tries to login, the user will be shown the errors they have in the field and if the username is not already registered.
        
        * Explanation of Login function in Accounts App
            * The function below shows the login view, It runs checks for user authentication before opening the view.
            * It then, posts the login form.
            * Another check is done to make sure form is valid, if it is valid the user is successfully logged in the user is then taken to the home page. 
            If the form is not valid it will not login the user and it shows the errors that caused the login to fail
    ```
    def login(request):
    """Return a login page"""
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        if request.method == "POST":
            login_form = UserLoginForm(request.POST)

            if login_form.is_valid():
                user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

                if user:
                    auth.login(user=user, request=request)
                    messages.success(
                        request,
                        "You have successfully logged in!"
                        )
                    return redirect(reverse('index'))
                else:
                    login_form.add_error(
                        None, 
                        "Your username or password is incorrect"
                        )
            else:
                login_form = UserLoginForm()
        return render(request, 'login.html', {'login_form': login_form})
        ```
        Below is the Test I wrote for Login view, I created the setUp for any tests that may be used in the tests.py
        It runs a test on the view of the login to make sure the url is working correctly

        ```
        class TestloginView(TestCase):
    # Sets up the testing to be down follwoing the setUp
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_login_view_POST(self):
        # runs test for login view
        response = self.client.post(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html', 'base.html')
        ```
* 
    * Register:
        * After coming to the home page,
        * I can either use the Navbar Register link or the Register option in Slide 1 of the Carousel
        * After clicking the Register button, I am directed to the Registration page that is triggered by the Registration view in the accounts app
        * The form is all required and asks for Email, username, password 1, and password confirmation
        
        * Explanation of Registration function in Accounts App
            * The function below shows the registration view, it initially checks if the user is authenticated, it will not open form if the user is already logged in.
            * It then, posts the registration form.
            * A check is done to make sure form is valid, 
            if it is valid the user is successfully registered you are automatically logged in and the user is then taken to the profile page. 
            If the form is not valid it will not register the user and it shows the errors that caused the registration to fail

 ```
    def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(
                    request,
                    "You have successfully registered"
                    )
                return redirect(reverse('profile'))
            else:
                messages.error(
                    request,
                    "Unable to register your account at this time"
                    )
            return redirect(reverse('all_products'))
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form
        })
```
* 
    * Profile:
        * After logging in or registering the profile view is immediatly available,
        * After clicking the profile button, I am taken to the profile page
        * On that page, the username and email are displayed, but the order_info and order_history functions are triggered 
        
        * Explanation of Profile, Order_Info, and Order_History functions in Accounts App
            * The profile function below shows the profile view, it runs a request for user info. That info is then displayed in profile.
            * The profile view caculates the order total to be displayed in the order list on the table in the profile
```
    @login_required
    def profile(request):
        if request.user:
            orders = Order.objects.filter(
                user=request.user,
                date__lte=timezone.now()
                ).order_by('-date')
            for order in orders:
                order.total = 0
                line_item = OrderLineItem.objects.filter(order=order)
                for item in line_item:
                    product = Product.objects.get(id=item.product.id)
                    order.total += product.price * item.quantity
        return render(request, "profile.html", {'orders': orders})
```


 The Order history function below shows the date and links the user to the specific order history


 ```
    @login_required
    def order_history(request):
        if request.user:
            orders = Order.objects.filter(
                user=request.user,
                date__lte=timezone.now()
                ).order_by('-date')
        return render(request, "profile.html", {'orders': orders})
```


        Order info Is triggered when the view details link is clicked. 
        It shows the details of the specific order. The function grabs the order when it is purchased, 
        it calculates the order total, keeps the product info, and displays it on a new page


```
    @login_required
    def order_info(request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.save()
        order_total = 0
        line_item = OrderLineItem.objects.filter(order=order)
        for item in line_item:
            product = Product.objects.get(id=item.product.id)
            order_total += product.price * item.quantity
        return render(
            request,
            "order-info.html",
            {'order': order,
            'line_item': line_item,
            'order_total': order_total,
            'product': product},
            )
```

* Logout
    * If the user needs to logout they can simply use the logout button in the Navbar, 
    The user is automatically logged out and taken to the home, it also gives a successfully logged out message.

```
    @login_required
    def logout(request):
        """Log the user out"""
        auth.logout(request)
        messages.success(request, "You have successfully been logged out")
        return redirect(reverse('index'))
```
* Products App - As a user I want to:
    * Browse all the products
        * On the home page, all of the products are displayed
        * This function grabs the products model
        * All_Products function is show below:
```
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

The following tests were written to test that the products are passing through correctly, and to test the products url

class TestProductUrls(TestCase):
    def test_url_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, all_products)


class ProductTests(TestCase):
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
```

* Searh App - As a user I want to:
    * Search for specific items
        * The search bar in the Navbar triggers the search function
        * The search function is also used in the second slide of carousel. This slide gives the user the option to shop Herbal or Shop Succulents
            * In the html I hid a search bar with those buttons with a set value to pull up the specified searches
            * Example below from products.html
```
<form class="width-removal" action="{% url 'search' %}" method="get">
    <input type="text" class="form-control d-none" value="Succulent" name="q">
    <a href="#shop"><button class="btn button-register-color arimo-font" type="search">Shop Succulents</button></a>
</form>

Here is also the search function, This function also triggers some JS that automatically scrolls down to view the search results that populate

def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products, "scroll_to_search_results": True})
```

* Cart App - As a user I want to: 
    * Add items to the cart
        * When viewing any product the add to cart option is available.
        * This button adds one product to the cart at a time
        * The Function shown below also allows the the user to add the same product to the quantity instead of adding a whole new product.
        * This also saves the cart id for the session so the cart items don't dissapear
```
def add_to_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    
    print(cart)

    request.session['cart'] = cart
    return redirect(reverse('index'))

```

* Checkout App - As a user I want to:
    * Purchase my items
        * After viewing the items in the cart, I click the checkout button
        * This button then triggers the 1st part of the checkout function which POSTs the order form
        * The form is split into 2 sections: Personal info and Payment info
        * This Form is preceded by an order summary, that gives the option to go back to cart
        * After the user has filled in the Order form, 2 buttons are shown that say "Review Order" or "Submit Payment"
        * Review Order toggles a modal to ask if order is correct
        * Submit payment then places the order with stripe And the order can then be seen in the Profile view and Oder Info view

        * The following function runs the checkout
            * The forms are posted
            * The time/date is captured, along with the validation if the form is valid
            * If the form is valid, the information from the order is saved to be displayed later in the order_info/Order_History
            * The checkout app also pulls the cart session to complete the order if the forms are valid
            * If there is an error in the forms, the order will not be processed until the errors are corrected and form is resubmitted.
            * If something is wrong with the card, an error message will displayed explaining the card is declined or not accepted
            
```
@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        now = timezone.now()
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = now

            order.user = request.user
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "You have successfully paid, Chek out your Profile for Order History")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request,
                "We were unable to take a payment with that card!"
            )
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(
        request,
        "checkout.html",
        {"order_form": order_form,
            "payment_form": payment_form,
            "publishable": settings.STRIPE_PUBLISHABLE})

```