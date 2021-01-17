## Testing
Testing involved viewing the website myself on a range of devices both in Chrome Dev tools and on physical Iphone, tablet and desktop devices.
As part of the testing procedure my peers reviewed the website and provided constructive comments.

In each of the main sections the required information has been provided and is accessible to the end user.
The layout of different sections expands into side by side columns on larger devices.
The functionality of media queries has been tested across all devices using Chrome Devtools.

The CRUD functionality of the Add / Edit / Delete operations have been tested by logging in with both normal user accounts and superuser accounts and performing these operations.
Back end form validation has been used to ensure input values are correctly entered and where possible user selection of location and dates have been restricted to only allow correct information selections.

The functionality of the Allauth Login / Logout / Signup operations have been tested by creating multiple dummy accounts in the database and confirming that these accounts have been setup and can perform their relevant tasks.

The functionality of the Stripe payment system has been tested to ensure form validation occurs and when the correct user information is entered that a payment, order and car booking are all created successfully. The Stripe webhook fucntion has also been checked to ensure that when a payment is processed the correct webhook is created.

The functionality of navigation links has been tested to ensure the user is taken to the correct page or location when navigating the site.

The responsiveness of the website has been tested across a range of devices (Galaxy S5, Iphone 5/6/7/8/X, IPad, IPad Pro and Desktop PC) using Chrome Dev tools.
The responsive design was also physically tested on personal Iphone, IPad, desktop and widescreen monitor devices.

W3C CSS & HTML Validators and ICI accessibilty checker were used to check the validity and formatting of code.

### Responsiveness
* **Plan:** The website needed to respond to different device sizes and to device orientation.
* **Implementation:** Bootstrap was employed to undertake a mobile first design with grid elements which change orientation based on screen width. I also created media queries to change the position of text at different screen sizes.
* **Result:** On small devices and medium to large devices the website responds well and the images and text can be easily viewed.
* **Verdict:** This test has passed and the site is responsive.

### Design
* **Plan:** The design of the site needs to be eye catching with simple to navigate sections and information.
* **Implementation:** The home page is bold and an informative svg image catches the users attention
* **Result:** The website catches the eye without overwhelming the user and provides a simple to use navigation with key skill and project information.
* **Verdict:** This test has passed.

### Ease of use
* **Plan:** The purpose of the site and its design needs to be easy to use
* **Implementation:** The how it works section explains to the user how CarLet works with links for the user to take the next steps
* **Result:** The purpose of the site is clearly explained
* **Verdict:** This test has passed.

### Registration
* **Plan:** The user can easily signup, login and logout
* **Implementation:** Allauth provides user registration and the relevant links are available to the user throughout the website
* **Result:** Dummy accounts for standard users and a super user account were setup and the functionality of these account operations tested. The login required decorator functionality was also tested to ensure that a user must be logged in to gain access to certain areas of the site and if they are not logged in they are redirected to the correct location.
* **Verdict:** This test has passed.

### Product searching
* **Plan:** The user can search for cars to hire on Carlet at any UK city and within a date range
* **Implementation:** The main index page search form allows searches at specific UK cities only as the places autocomplete is restricted by the google javascript settings. The user cannot enter incorrect date information as this is also resticited in the date range javascript
* **Result:** Searches can be carried out correctly and the required search results are provided.
* **Verdict:** The test has passed.

### CRUD (Create, Read, Update, Delete) Functionality
* **Plan:** Provide the user with the ability to add a car to Carlet, Edit or Delete a car
* **Implementation:** The website Dashboard provides links to forms which allow CRUD functionality. A boolean value is set in the car model when the normal user removes the car from the database, this way the previous order and booking information is not lost as the car is not deleted from the database. A superuser can permanently delete a car from the database.
* **Result:** The users can add, edit, remove and delete cars from Carlet
* **Verdict:** This section has passed the test.