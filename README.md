<h1 align="center">Car-Let</h1>

This website allows users to search a list of cars for hire by location.
Users can click on an available car to see additional car details and then hire that car if they wish to do so.
Users can also upload their car to the website to make it available for hire.
Users can create, view, update and delete an account when required.
Visitors can also view their cart and easily checkout a car.

## UX
### User Stories
![User Stories](/static/docs/project_setup.ods)

### Strategy
The Carlet website will provide visitors with an easy to use search facility where they can find cars to hire in their location.

Users will have the ability to upload a car to let / hire out to other site users.

Users will 

Users will find projects displayed in tiles with an image of each particular webpage. Each tile will contain a link to another webpage with greater project detail.

This portfolio website will be aimed at a range of demographics from the field of web development and potential clients interested in working on new projects. 
As a result of this wide range of users the site must be simple to use and laid out in a concise manner.

### Scope
Website key features include the following;



### Structure
I wnat to use bright but neutral colors to attract users from a variety of demographics to the website.
![Color Palette](/static/docs/carlet1.pdf)

### Surface


### Wireframes
![Home Desktop](/static/wireframes/Home.png)
![Home Tablet](/static/wireframes/Home_tablet.png)
![Home Mobile](/static/wireframes/Home_phone.png)
![Car details Desktop](/static/wireframes/Car_details.png)
![Car details Tablet](/static/wireframes/Car_details_tablet.png)
![Car details Mobile](/static/wireframes/Car_details_phone.png)
![Sign Up](/static/wireframes/Sign_up_In.png)
![Sign Up Tablet](/static/wireframes/Sign_up_In_tablet.png)
![Sign Up Mobile](/static/wireframes/Sign_up_in_phone.png)
![Search Logged in Desktop](/static/wireframes/Search_logged_in.png)
![Search Logged in Tablet](/static/wireframes/Search_logged_in_tablet.png)
![Search Logged in Mobile](/static/wireframes/Search_logged_in_phone.png)
![Car details Logged in Desktop](/static/wireframes/Car_details_logged_in.png)
![Car details Logged in Tablet](/static/wireframes/Car_details_logged_in_tablet.png)
![Car details Logged in Mobile](/static/wireframes/Car_details_logged_in_phone.png)
![My account Desktop](/static/wireframes/My_account.png)
![My account Tablet](/static/wireframes/My_account_tablet.png)
![My account Mobile](/static/wireframes/My_account_phone.png)
![Hire history Desktop](/static/wireframes/Hire_history.png)
![Hire history Tablet](/static/wireframes/Hire_history_tablet.png)
![Hire history Mobile](/static/wireframes/Hire_history_phone.png)
![My Listings Desktop](/static/wireframes/My_listings.png)
![My Listings Tablet](/static/wireframes/My_listings_tablet.png)
![My Listings Mobile](/static/wireframes/My_listings_phone.png)
![Checkout Desktop](/static/wireframes/Checkout.png)
![Checkout Tablet](/static/wireframes/Checkout_tablet.png)
![Checkout Mobile](/static/wireframes/Checkout_phone.png)
![Logout Desktop](/static/wireframes/Log_out.png)
![Logout Tablet](/static/wireframes/Log_out_tablet.png)
![Logout Mobile](/static/wireframes/Log_out_phone.png)

### Technologies used
1. HTML
2. CSS
3. Javascript
4. [Bootstrap](https://getbootstrap.com/)
5. [Googel Fonts](https://fonts.google.com/)
6. [Font Awesome](https://fontawesome.com/)
7. [Auto Prefixer](https://autoprefixer.github.io/)
8. [JQuery](https://jquery.com/)
9. [Popper.js](https://popper.js.org/)
10. [Python](https://www.python.org/)
11. [Inkscape](https://inkscape.org/)

## Features
### Existing features

### Information Architecture

### Project collection

### File structure

### Features to implement

## Testing
Please see the TEST.md file at this link [TEST.md](TEST.md) to understand how the Car-Let website was tested.

## Deployment
This project was developed using the GitPod IDE, version controlled by committing to git and pushing to GitHub via the GitPod IDE.
The deployment instructions have been written for a macOS specifically, therefore the commands and installation may differ slightly for your machine.

### How to run this project locally
The following must be installed on your machine;
* PIP
* Python 3
* GitHub

#### instructions
1. Open the repository located at
2. Click on **Clone or Download** and copy the URL
3. In your IDE enter the command 
4. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. To do this enter the command
5. Activate the virtual environment with the command 
6. If required upgrade pip locally with the command
7. Install all required packages from the requirements file with the command
8. In your local IDE create a file called env.py
9. Inside this file create a SECRET_KEY variable, a MONGO DBNAME a MONGO_URI and an EMAILJS_KEY.
10. In MongoDB create a database called Portfolio, with 2 collections called Skills and Projects. You will find example JSON structures for these collections in the data/schemas folder
11. You can now run the application with the command
12. The project can be viewed at **Insert http link**

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
IP | 0.0.0.0
PORT | 5000
EMAILJS_KEY | <youe_emailjs_key>
MONGO DBNAME | <your_mongodb_name>
MONGO_URI | <mongo_uri>
SECRET_KEY | <your_secret_key>

9. Start a web process with the IDE command `heroku ps:scale web=1`
10. The site is now successfully deployed

## Note for the assessor
To test the CRUD functionality of this project

URL | Username | Password
----|----------|---------
https://conal-walsh-portfolio.herokuapp.com/ | Admin | Admin1234

## Acknowledgements
I would like to thank my mentor Simen for his valuable advice and guidance throughout the project.

**This is for educational use**
