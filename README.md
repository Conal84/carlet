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
The Portfolio website will provide users with an easy to access skills and project information about the site adminstrator.

Users will be presented with a strong hero section which will showcase skills in web design and javascript.

Users will also be presented with an animated skills section with eye catching progress bars.

Users will find projects displayed in tiles with an image of each particular webpage. Each tile will contain a link to another webpage with greater project detail.

This portfolio website will be aimed at a range of demographics from the field of web development and potential clients interested in working on new projects. 
As a result of this wide range of users the site must be simple to use and laid out in a concise manner.

### Scope
Website key features include the following;



### Structure
I want to keep the site as minimalist and clutter free as possible so that it is easy to use for the wide ranging demographic and so users are not overwhelmed with information.
Information will be provided to users in a concise, straight forward manner.

The mobile first design will arrange information in single full width columns to allow content to be read easily.
On larger tablet and desktop display information will be arranged in additional columns using Bootstraps responsive grid design.

Information will be grouped in 4 key areas;
* Hero - provides an eye catching background image with introductory information about me
* Skills - provides key skills information via progress bars
* Projects - provides initial, concise project information with links to more detailed views
* Contact - provides an easy method to send me a direct email

### Surface
I want the colors used on the site to grab the users attention without being too acute.

The primary colours for the website are black #0b0a07, yellow #ffcd24 used to grab the attention of visitors.
Contrasting white #fff and grey #eaecec are used to display text information and to provide background segregation between key areas.
A secondary softer blue highlight color #1478a3 has then been used to make key elements stand out on the page and to grab the attention of the user without overwhelming.

I have used Open Sans font throughout the website as it has a simplistic style.
I have used Raleway font for the headings as this font makes the heading stand out and grabs the users attention.
I have also used an Inconsolata font as it mimics a faux coding style font in the hero section.

I have used Inkscape to design an svg image which I used for my portfolio logo and favicon.

### Wireframes
![Home Desktop](/wireframes/Home.png)
![Home Tablet](/wireframes/Home-tablet.png)
![Home Mobile](/wireframes/Home-mobile.png)
![Contact Desktop](/wireframes/Contact.png)
![Contact Tablet](/wireframes/Contact-tablet.png)
![Contact Mobile](/wireframes/Contact-mobile.png)
![Admin Desktop](/wireframes/Admin.png)
![Admin Tablet](/wireframes/Admin-tablet.png)
![Admin Mobile](/wireframes/Admin-mobile.png)
![Logged in Desktop](/wireframes/Logged-in.png)
![Logged in Tablet](/wireframes/Logged-in-tablet.png)
![Logged in Mobile](/wireframes/Logged-in-mobile.png)
![Skills delete Desktop](/wireframes/Skills-delete.png)
![Skills delete Tablet](/wireframes/Skills-delete-tablet.png)
![Skills delete Mobile](/wireframes/Skills-delete-mobile.png)
![Skills edit Desktop](/wireframes/Skills-edit.png)
![Skills edit Tablet](/wireframes/Skills-edit-tablet.png)
![Skills edit Mobile](/wireframes/Skills-edit-mobile.png)
![Skills add Desktop](/wireframes/Skills-add.png)
![Skills add Tablet](/wireframes/Skills-add-tablet.png)
![Skills add Mobile](/wireframes/Skills-add-mobile.png)
![Portfolio delete Desktop](/wireframes/Portfolio-delete.png)
![Portfolio delete Tablet](/wireframes/Portfolio-delete-tablet.png)
![Portfolio delete Mobile](/wireframes/Portfolio-delete-mobile.png)
![Portfolio edit Desktop](/wireframes/Portfolio-edit.png)
![Portfolio edit Tablet](/wireframes/Portfolio-edit-tablet.png)
![Portfolio edit Mobile](/wireframes/Portfolio-edit-mobile.png)
![Portfolio add Desktop](/wireframes/Portfolio-add.png)
![Portfolio add Tablet](/wireframes/Portfolio-add-tablet.png)
![Portfolio add Mobile](/wireframes/Portfolio-add-mobile.png)
![Portfolio see more Desktop](/wireframes/Portfolio-see-more.png)
![Portfolio see more Tablet](/wireframes/Portfolio-see-more-tablet.png)
![Portfolio see more Mobile](/wireframes/Portfolio-see-more-mobile.png)

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
11. [MongoDB](https://www.mongodb.com/)
12. [EmailJS](https://www.emailjs.com/)
13. [Inkscape](https://inkscape.org/)
14. [Imgbb](https://imgbb.com/)

## Features
### Existing features
* Home page with navbar, hero section, skills section, portfolio section, contact section and footer
    * Navbar has links with Home, About, Portfolio, Contact and a logo for my portfolio page made in inkscape with a link to the home page
    * Hero section is a animated canvas. The animation sweeps 2 colored lines across the page and contains colored polygons which are seperated by those lines. The hero section also contains faux code sections which detail some of my coding skills.
    * About/Skills section contains a paragraph with some of my background information and interests and an animated skills progress bar
    * Portfolio section contains websites introductory images with brief descriptions. Images are stored on the Imgbb.com website and linked to the MongoDB database.
    * Contact section contains a message and a Get in touch button which brings up a form modal, this form sends an email to my personal email address
    * Footer has links to my Github and a dummy Linkedin page

* Portfolio Section - See more
    * When a visitor clicks on a project see more button they are taken to a project specific page with a link to the Github and dedicated page for that website
    * The visitor can also see some further images of the project in a carousel

* Contact Section - Get in touch
    * A visitor can send me a personal email to discuss my work or future projects by completing this contact form and pressing the send button

* Admin page
    * A page where the admin user can submit username and password

* Home page - Logged in
    * At the page the admin user can perform CRUD operations on the skills section and portfolio section of the webpage
    * The admin user can Create, Update or Delete skills or projects from the webpage
    * Deleting skills or projects displays a modal which ask for user confirmation prior to deleting information

* Edit skill
    * Displays a form which is prepopulated with the skill data
    * Skill data can be updated and submitted
    * Upon submission the user is returned to the Home page where they can see the changes made

* Add skill
    * Displays a form which contains a placeholder for the skill icon so the user can see the format required for the skill icon
    * The skill name, skill percentage and skill icon can be added

* Edit project
    * Displays a form which is prepopulated with the project information
    * Project information can be updated and submitted
    * Upon submission the user is returned to the Home page where they can see the changes made

* Add project
    * Displays a form with empty fields where the user can add new project information and submit

* 404 page
    * An error 404 page with a link to the home page

### Information Architecture
This project uses the NoSQL database MongoDB with the following database design structure and variables

### Project collection
![Information architecture](/data/schemas/Database-design.png)

Prior to beginning work on the project the below file structure was laid out to understand how the various webpages would link together

### File structure
![File structure](/data/schemas/File-structure.png)

### Features to implement
Future features will include additonal skills and more showcase projects as I build more websites.

## Testing
Please see the TEST.md file at this link [TEST.md](TEST.md) to understand how the Portfolio website was tested.

## Deployment
This project was developed using the GitPod IDE, version controlled by committing to git and pushing to GitHub via the GitPod IDE.
The deployment instructions have been written for a macOS specifically, therefore the commands and installation may differ slightly for your machine.

### How to run this project locally
The following must be installed on your machine;
* PIP
* Python 3
* GitHub
* A [MongoDB](https://www.mongodb.com/) account or MongoDB running locally on your machine.
    * See how to signup for a MongoDB account [here](https://www.mongodb.com/cloud/atlas/signup)

#### instructions
1. Open the repository located at [https://github.com/Conal84/Portfolio](https://github.com/Conal84/Portfolio)
2. Click on **Clone or Download** and copy the URL
3. In your IDE enter the command `git clone https://github.com/Conal84/Portfolio`
4. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. To do this enter the command `python3 -m .venv venv`
5. Activate the virtual environment with the command `.venv\Scripts\Activate`
6. If required upgrade pip locally with the command `pip install --upgrade pip`
7. Install all required packages from the requirements file with the command `pip -r requirements.txt`
8. In your local IDE create a file called env.py
9. Inside this file create a SECRET_KEY variable, a MONGO DBNAME a MONGO_URI and an EMAILJS_KEY.
10. In MongoDB create a database called Portfolio, with 2 collections called Skills and Projects. You will find example JSON structures for these collections in the data/schemas folder
11. You can now run the application with the command `python3 app.py`
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
