<h1 align="center">Car-Let</h1>

[Carlet](https://carlet-app.herokuapp.com/) The car sharing website.
Carlet users can search a list of cars for hire by location.
Users can click on an available car to see additional car details and then hire that car if they wish to do so.
Users can also upload their car to the website to make it available for hire.
Users can create, view, update and delete an account when required.
Visitors can also view their cart and easily checkout a car.

## UX
### User Stories
#### Visitor (Not Signed up user)
As a site visitor I want to carry out a search so I can see what products are available

As a site visitor I want to easily understand how the site works and what it does so I can use the site quickly and easily make purchases

As a site visitor I want to easily create an account and login to my account so I can access additional site functionality

#### User (Signed up user)
As a site user I want to be able to view a list of products so I can easily choose what I want

As a site user I want to be able to view individual product details so I can see more information and make a choice

As a site user I want to be able to view the cost of purchases at any time so I can easily see the cost of item I have chosen

As a site user I want to be able to login to my account so I can see my account details, current and previous purchases

As a site user I want to be able to logout of my account so I can securely leave the site

As a site user I want to be able to easily recover my password if forgotten so I can regain site access

As a site user I want to be able to receieve email confirmation after sign up so I can confirm successful registration

As a site user I want to be able to easily add a car to the hire car system so I can quickly and easily use the site

As a site user I want to be able to edit a current car in the system so I can update my car information

As a site user I want to be able to see my previous orders and car booking history so I can remind myself of previous site interactions

As a site user I want to be able to view items in my bag to be purchased so I can easily see what I am purchasing

As a site user I want to be able to remove items from my bag which I no longer want so I can easily change my requested items

As a site user I want to be able to delete a car from the car hire system so I can remove a product which is no longer available

As a site user I want to be able to easily enter my payment information so I can make a payment with ease

As a site user I want to be able to feel my personal payment information is secure and safe so I can have peace of mind when making a purchase

As a site user I want to be able to view an order confirmation after checkout so I can feel secure that the transaction has taken place

As a site user I want to be able to receieve an email confirmation after placing an order so I can feel secure that the transaction has taken place


### Strategy
The Carlet website will provide visitors with an easy to use search facility where they can find cars to hire in their location.

Users will have the ability to upload a car to let / hire out to other site users.

Users will can create a personal account where they can login to see their current and previous car hires and car lets.

Users can easily add products to their cart, view their cart total, cart items and can use a checkout to enter their payment details and confirm their order.

Users orders will be confirmed by a personal email sent to their email account.

Admin users will be able to create, view, update or delete products or users from the website by logging in with admin rights.

This portfolio website will be aimed at a range of demographics, both male and female from 18 years plus.
As a result of this wide range of users the site must be simple to use and laid out in a concise manner with a simple explanation of how the car hiring process works.
The color palette of the site must also appeal to these demographics.

### Structure
I want to keep the site as minimalist and clutter free as possible so that it is easy to use for the wide ranging demographic and so users are not overwhelmed with information. Information will be provided to users in a concise, straight forward manner.

The mobile first design will arrange information in single full width columns to allow content to be read easily. On larger tablet and desktop display information will be arranged in additional columns using Bootstraps responsive grid design.

### Surface
I want to use bright but neutral colors to attract users from a variety of demographics to the website.
![Color Palette](/static/docs/carlet_colors.png)

The primary colours for the website are white #ffffff, purple #7510F7 and pink #DC04B4 used to grab the attention of visitors. A secondary softer blue highlight color #6CD4FF has then been used to make key elements stand out on the page and to grab the attention of the user without overwhelming.

I have used Nunito Sans font throughout the website as it has a simplistic style. I have used Roboto font for the headings as this font makes the heading stand out and grabs the users attention.

I have used Inkscape to design and modify svg images which I used for the main page background image and on the how it works pages to explain in simple terms to site visitors how to use CarLet.

### Wireframes
* [Home Desktop](/static/wireframes/Home.png)
* [Home Tablet](/static/wireframes/Home_tablet.png)
* [Home Mobile](/static/wireframes/Home_phone.png)
* [Car details Desktop](/static/wireframes/Car_details.png)
* [Car details Tablet](/static/wireframes/Car_details_tablet.png)
* [Car details Mobile](/static/wireframes/Car_details_phone.png)
* [Sign Up](/static/wireframes/Sign_up_In.png)
* [Sign Up Tablet](/static/wireframes/Sign_up_In_tablet.png)
* [Sign Up Mobile](/static/wireframes/Sign_up_in_phone.png)
* [Search Logged in Desktop](/static/wireframes/Search_logged_in.png)
* [Search Logged in Tablet](/static/wireframes/Search_logged_in_tablet.png)
* [Search Logged in Mobile](/static/wireframes/Search_logged_in_phone.png)
* [Car details Logged in Desktop](/static/wireframes/Car_details_logged_in.png)
* [Car details Logged in Tablet](/static/wireframes/Car_details_logged_in_tablet.png)
* [Car details Logged in Mobile](/static/wireframes/Car_details_logged_in_phone.png)
* [My account Desktop](/static/wireframes/My_account.png)
* [My account Tablet](/static/wireframes/My_account_tablet.png)
* [My account Mobile](/static/wireframes/My_account_phone.png)
* [Hire history Desktop](/static/wireframes/Hire_history.png)
* [Hire history Tablet](/static/wireframes/Hire_history_tablet.png)
* [Hire history Mobile](/static/wireframes/Hire_history_phone.png)
* [My Listings Desktop](/static/wireframes/My_listings.png)
* [My Listings Tablet](/static/wireframes/My_listings_tablet.png)
* [My Listings Mobile](/static/wireframes/My_listings_phone.png)
* [Checkout Desktop](/static/wireframes/Checkout.png)
* [Checkout Tablet](/static/wireframes/Checkout_tablet.png)
* [Checkout Mobile](/static/wireframes/Checkout_phone.png)
* [Logout Desktop](/static/wireframes/Log_out.png)
* [Logout Tablet](/static/wireframes/Log_out_tablet.png)
* [Logout Mobile](/static/wireframes/Log_out_phone.png)

### Technologies used
#### Tools
* [Auto Prefixer](https://autoprefixer.github.io/)
* [JQuery](https://jquery.com/)
* [Popper.js](https://popper.js.org/)
* [Inkscape](https://inkscape.org/)
* [GIMP](https://www.gimp.org/)
* [InkScape](https://inkscape.org/)
* [Django](https://www.djangoproject.com/)
* [Balsamiq](https://balsamiq.com/)
* [SweetAlert2](https://sweetalert2.github.io/)
* [Heroku](https://www.heroku.com/)
* [Stripe](https://stripe.com/)
* [AWS_S3](https://aws.amazon.com/)

#### Databases
* [PostgreSQL](https://www.postgresql.org/) for production database
* [SQlite3](https://www.sqlite.org/index.html) for development database

#### Libraries
* [Bootstrap](https://getbootstrap.com/)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/)
* [JQuery](https://jquery.com/)

##### Languages
* HTML
* CSS
* Javascript
* Python

## Features
Website key features include the following;

A user admin section where users can login, logout and sign up.

A How It Works section where new visitors to the site can easily learn how CarLet works

A search form which allows site users to search for cars in a UK city between certain user provided hire dates. Car availability is checked against the users search dates, search location and any existing bookings for a car.

An All Cars page which display all possible cars availabe to hire for the users search criteria

A Car Detail section which displays information about a particular car and includes a Google Map so the user can find the car location easily.

Pages where the user can add additional products; Car Insurance and Car Breakdown Support

A Checkout page where the user can place an order and enter their payment information securely.

An order confirmation page where the user can see their confirmed purchase.

A Dashboard page with links to additional useful user information where users can view their orders, bookings, profile information, add a new car and edit or remove their car.

Admin superusers can view all cars in the database and delete any specific car from the database.

### Features to implement
Futue featues to implement include a star rating system where users can allocate star ratings to the people they have hired cars from.

An car add security feature would not immediatley allow users to upload their car information and photos to the site. Instead the new car details would be uploaded to an admin area for admin approval prior to uploading to the site.

Add some code to resize any car images uploaded by user so they are not too large.

## Testing
Please see the TEST.md file at this link [TEST.md](TEST.md) to understand how the CarLet website was tested.

## Deployment
This project was developed using the GitPod IDE, version controlled by committing to git and pushing to GitHub via the GitPod IDE.
The deployment instructions have been written for a macOS specifically, therefore the commands and installation may differ slightly for your machine.

### How to run this project locally
The following must be installed on your machine;
* PIP
* Python 3
* GitHub

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services: 
* Stripe - for payment processing
* AWS and set up an S3 bucket - for static file storage
* GMail - to send emails

#### instructions
1. Open the repository located at [https://github.com/Conal84/carlet](https://github.com/Conal84/carlet)
2. Click on **Clone or Download** and copy the URL
3. In your IDE enter the command `git clone https://github.com/Conal84/carlet`
4. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. To do this enter the command `python3 -m .venv venv`
5. Activate the virtual environment with the command `.venv\Scripts\activate`
6. If required upgrade pip locally with the command `pip3 install --upgrade pip`
7. Install all required packages from the requirements file with the command `pip3 -r requirements.txt`
8. In your local IDE create the required environment variables;

KEY | VALUE
----|------
SECRET_KEY | <enter_django_secret_key_here>
STRIPE_SECRET_KEY | <enter_Stripe_secret_key_here>
STRIPE_PUBLIC_KEY |<enter_Stripe_public_key_here>
STRIPE_WH_SECRET | <enter_Stripe_webhook_secret_here>
DATABASE_URL | <enter_postgres_database_url_here>
DEVELOPMENT | <enter_True_here>

* Note: DEVELOPMENT environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

9. Migrate the admin panel models to create your database template with the terminal command `python3 manage.py migrate`
10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password `python3 manage.py createsuperuser`
11. You can now run the program locally with the following command `python3 manage.py runserver`
12. Once the program is running, go to the local link provided and add /admin to the end of the url. Here log in with your superuser account.

### Heroku Deployment
1. Create a new app on the [Heroku website](https://www.heroku.com/#)
2. Link your local git repo to the Heroku app
    * Go to the Heroku app settings , find the Heroku Git URL and copy it
    * In your IDE use command `git remote add heroku *paste heroku git url here*`
3. In your IDE create a requirements.txt file using the command `pip3 freeze --local > requirements.txt`
4. Create a Procfile the the command `echo web: python app.py > Procfile`
5. `git add` and `git commit` the new requirements and Procfile, then `git push` to GitHub
6. `git push -u heroku master` command then pushes code to the Heroku app
7. Set the config variables in the Heroku app by clicking Settings > Reveal Config Vars
8. Add the following config vars

KEY | VALUE
----|------
AWS_ACCESS_KEY_ID | <your_aws_key>
AWS_SECRET_ACCESS_KEY | <your_secret_key>
DATABASE_URL | <your_postgres_database_url>
EMAIL_HOST_PASS | <your_email_host_pass>
EMAIL_HOST_USER | <your_email_host_user>
SECRET_KEY | <your_django_secret_key>
STRIPE_PUBLIC_KEY | <your_stripe_secret_key>
STRIPE_SECRET_KEY | <your_stripe_secret_key>
STRIPE_WH_SECRET | <your_stripe_secret_key>
USE_AWS | <set_to_True>

9. From the command line of your local IDE:

Enter the heroku postres shell
Migrate the database models
Create your superuser account in your new database
Instructions on how to do these steps can be found in the heroku devcenter documentation.

10. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

11. Once the build is complete, click the "View app" button provided.

12. From the link provided add /admin to the end of the url, log in with your superuser account.

## Acknowledgements
I would like to thank my mentor Simen for his valuable advice and guidance throughout the project.

**This is for educational use**
