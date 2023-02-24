# **Eatopia** 
![Eatopia](/static/images/am-i-responsive.png)
# **Eatopia**
Eatopia is a website where people can share their favourite recipes for others to try and also where they can find tasty recipes to use themselves. Users can create an account and create recipes, view other users recipes and also comment and like on recipes. 

[View live project here](https://eatopia.herokuapp.com/)

## **Introduction** 

When initially planning this project I first had to decide on what features the user would need so that I could I could decide on what type of site I was making. I then constructed wireframes to format the design of the site. I then turned my focus to the database models. Planning and preparation was key when constructing this site. 

## **Project Goals**

My goal for this site were to create a user friendly website were people can get inspiration on recipe ideas. The user can create an account to share his or her favourite recipe and also interact with other users recipes. 

## **Site Owner Goals**

* Provide the user with and easy to use professional website.
* Interact with recipes the may be interested in.
* Provide recipes for users that are budget friendly. 

**User Stories**

*Applies to site users with and/or without account:*
* As a site user I can see a list of recipes so that I can choose which one to view. 
* As a site user I can click on a recipe so that I can view it in full. 
* As a site user I can register an account so that I can have access to the site. 
* As a site user I can like or unlike a recipe so that I can interact with the content. 
* As a site user I can comment recipes so that I can be part of the conversation.  
* As a site user I can view the comments for a recipe so that I can see read the conversation.
* As a site user I can view number of likes for a specific recipe so that I can see which recipes are more popular.
* As I site user I can read about the site to understand what type of recipes will be available and be encouraged to visit the site again. 
* As a site user I can create, read, update and delete posts so that I can manage my content. 
* As a site user I can log in/out so that I can interact with the site.

*Applies to site Admin/SuperUser:*
 * As Admin I can tell site users about delicious,budget friendly recipes so that users will be encouraged to visit the site again.
* As Admin I can create, read, update and delete posts so that I can manage my content.
* As Admin I can delete recipes if inappropiate so that the content of the site is relevant.

**Design Goals**

* A site that works on all devices. 
* Clean and sophisticated design to enhance user experience. 
* Easy to understand and use.
* The style aims to give the user such a good experience that they will want to visit the site again. 

**Design Choices**

* Font

As Font I chose Roboto for all my headings for its simple but yet stylish design. To keep the site neat I chose to use Lato for all other text on the site. 
font-family: 'Roboto', serif;
font-family: 'Lato', sans-serif;

* Color Scheme

For the colour scheme I kept it very simple, I used mainly white and light grey. The font is black so it is easily read. As the site with feature a lot of food images I wanted the images to stand out and be the main eye-catcher. When viewing the site i wanted the food to be the main attraction.

- background-color: #F9FAFC;
- background-color: #fff;
- Black: #000000 

![Logo](/static/images/eatopia_logo.png)
 
* Logo Eatopia

I used [canva.com](https://www.canva.com/) to create my logo. I wanted a clean logo that goes well with the content of the site. I wanted a red heart to symbolise the love for food. 

**Wireframes**

Wireframes were used using Balsamiq Wireframes. The aim was to get a basic layout of all the componets to help me in the design process. 

![Home](/static/images/wireframe_1.png)

![About](/static/images/wireframe_2.png)

![Add Recipe](/static/images/wireframe_3.png)

![Register](/static/images/wireframe_4.png)

![Login](/static/images/wireframe_5.png)

## Information Architecture ##

* Database Models 

![Entity Relationship Diagram](/static/images/erd.png)

* Site Map 

![Site Map](/static/images/Site-map.png)

# Features #

## Design Features 

### Header
* The header contains the Navigation Bar which remains present on all pages of the site. The Eatopia logo is also located to the left of the Navigation Bar, clicking on the logo will take you back to the home page of the site. Page links are located on the navigation bar and these change depending on whether the user is logged in or logged out. For smaller devices the nabigation bar transforms into a Burger Button which contains the page links. 

### Home Page 
* When visiting the site you are greeted by an image of food and a jumbotron message. Below the image is a prompt for the site user to either login or register on the site. If you are logged in already then the user will be greeted with thier username. 

### Footer
 * The footer is basic and simple as to not distract from the main home page. It contains copyright information and icon links to various social media pages. 

## Existing features

* **Header Logo** appears on every page for consistency and easy navigation, clicking the logo takes you back to the home page. 
* **Header Nav-Bar** appears on every page for consistency and easy navigation, the Nav-Bar toggles on smaller screens for better user experience. The Nav-Bar presents different links if the user is logged in or not.  
![Navbar](/static/images/navbar.png)

* **Home Page Image** is to greet the site user and instantly provide the purpose of the site. 
* **Home Page Welcome Text** is to give immediate guidance to the site user. If the user is logged in they will be greated by their username, if not there are links to Login/Register an account.
![Home page image and text](/static/images/welcome.png) 

* **Recipe Cards** are presented on the home page. The 
cards are paginated by six, i.e if there are more than six recipes on the site they will be displayed on another site. Arrows will point the user in the right direction for good user experience. The cards hold information of the recipe title, author, created on, number of likes and an image. If the user has not chosen a specifik image a placeholder image will be displayed. 
![Recipe Cards](/static/images/recipe-cards.png)

* **Recipe Form** can be used by logged in users. Here users who holds an account can add their own recipes, and also edit their own recipes.
![Add Recipe](/static/images/add-recipe.png) 

* **Comment Form** is displayed underneath each recipe when viewed in full. Logged in users can comment recipes. 
![Comment](/static/images/comment.png)

* **Comment Section** is where all users, logged in or not can read all comments, who wrote them and when. 
* **Like/Unlike Button** appears on the recipe site and all logged in users can like/unlike recipes. Number of likes are also displayed for all users to see so users can determine popularity of recipes.. 
* **About Page** gives the user information about the topic of the site. 
![About Page](/static/images/about.png)

* **Recipe Page** is displayed when clicked on a recipe. Here all users, logged in or not, can view details about the recipe. This page also includes features to like and comment if you are a logged in user. If you are the author of the recipe, from here you can be redirected to edit/delete your recipe.  
* **Edit/Delete recipe** is where the creator of the recipe can manage their recipes by editing or deleting them. 
![Edit/delete](/static/images/manage.png)

* **Login Page** here users who already have created an account can log in. Users can also choose to be "remembered", a feature so that they do not have to enter their login credentials each time they log in, included for better UX.
![Login](/static/images/sign-in.png) 

* **Register Page** is where new users can create a new account so that they can interact with the site. By creating a username, providing optional email and a required password an account is easily created. 
![Register](/static/images/sign-up.png)

* **Logout** is a page for the user to confirm their intention to log out of their account. If the user clicks the sign out button, they are then redirected to the home page.
![Logout](/static/images/sign-out.png)

**Future Features**

* **Search Recipes Option**

This would allow users to search for recipes or recipe keywords e.g Chicken recipes. Also if a user enjoys a particular authors recipes they could search for the author name. 

* **Individual Profiles**

This would aloow the user to create a profile about themselves and share information such as cooking tips and preferences. 

* **Video Feature**

This would allow users to upload videos of themselves actually cooking the recipe. Allowing those watching to get a better understanding of cooking the recipe. 

# **Testing**

## Testing User Stories
**User Stories**

*Applies to site users with and/or without account:*
1.  As a site user I can see a list of recipes so that I can choose which one to view. 
   * Recipes are clearly visible on the home page. A preview of the recipe is also visible. Recipes are paginated by 6 and if there is more than 6 on a page then a new page is created. 
2.  As a site user I can click on a recipe so that I can view it in full. 
   * When a site user clicks a recipe card, the recipe will be displayed in full. The user can now see full ingredients list, instructions and cooking time. The user can aslo see who created the recipe and when it was created. 
3.  As a site user I can register an account so that I can have access to the site.
   * The user can register an account by entering a username, email(optional) and password. The user can also choose to be remembered as to not have to enter details every time. 
4.  As a site user I can like or unlike a recipe so that I can interact with the content.
   * As a registered user, the individual can like or unlike a recipe to show popularity, this is done by easily clicking the love heart icon. 
5.  As a site user I can comment recipes so that I can be part of the conversation. 
   * As a registered user, I can comment on any recipe to share my thoughts with other site users. 
6.  As a site user I can view the comments for a recipe so that I can see read the conversation.
   * As a site user, registered or unregistered, I can view all comments on any recipe. 
7.  As a site user I can view number of likes for a specific recipe so that I can see which recipes are more popular.
   * As I sight user, registered or unregistered, I can view the likes of a particular recipe either from the recipe card or by clicking into the recipe. 
8.  As I site user I can read about the site to understand what type of recipes will be available and be encouraged to visit the site again. 
   * As a site user, I can click into the About section and view what the site is about and what it aims to achieve. 
9.  As a site user I can create, read, update and delete posts so that I can manage my content. 
   * As a registered user I can create a recipe of my choosing, read other recipes, update my recipe if I desire and also delete my recipe if I desire. 
10.  As a site user I can log in/out so that I can interact with the site.
   * as a site user I can log in to my account using my username and password, and I can sign out buy clicking the log out button on the navigation bar. 

*Applies to site Admin/SuperUser:*
1.  As Admin I can tell site users about delicious,budget friendly recipes so that users will be encouraged to visit the site again.
   * By having an eye catching welcome page and by having an about page, I can encourage users to view what the page is aiming to achieve and enable them to view recipes.
2.  As Admin I can create, read, update and delete posts so that I can manage my content.
   * As an Admin it is a key responsibily to provide ey cathing, delicious recipes to get users involved and wanting to use the site. 
3.  As Admin I can delete recipes if inappropiate so that the content of the site is relevant.
   * As admin I can delete any recipe that is not suitable for the page as to keep with the ethos and goals of the site. 

## Manual Testing 

### Navigation Bar

#### Navigation Bar 

* Expected Outcome: The navigation bar should be visible on every page of the site. If page is rendered on smaller screens the navigation bar should toggle to a Burger Button for better user experience. 
* Test: Visit every page of the site to check if navigation bar is visible. View the navigation bar on different size screens to check responsiveness of navigation bar and toggle function and ensure Burger Button is rendered. 
* Result: The navigation bar is visible on every page of the site. When viewed on smaller screens a Burger Button appears and the the links are toggled for better user experience. 
* Verdict: Code functions as intended.

#### Logo

* Expected Outcome: When clicking the Eatopia logo, the user should be redirected to home page. 
* Test: I tried clicking the Eatopia logo from all different pages on the site, both as logged in user and as a logged out user. 
* Result: Every time I clicked the logo I was redirected to home page. 
* Verdict: Code functions as intended.

#### Home Link

* Expected Outcome: When clicking on Home link, the user should be redirected to home page. 
* Test: I tried clicking the Home link from all different pages on the site, both as logged in user and as a logged out user. 
* Result:Every time I clicked the Home link I was redirected to home page. 
* Verdict: Code functions as intended.

#### About Link

* Expected Outcome: When clicking on About link, the user should be redirected to About page.
* Test: I tried clicking the About link from all different pages on the site, both as logged in user and as a logged out user.
* Result: Every time I clicked the About link I was redirected to About page.
* Verdict: Code functions as intended.

#### Add Recipe Link

* Expected Outcome: When clicking on Add Recipe, the user should either be redirected to Add Recipe page if logged in or redirected to the Login page if not. 
* Test: I tried clicking the Add Recipe link both as logged in user and as user not logged in. 
* Result: When clicking the Add Recipe link as logged in the user is redirected to Add Recipe. If the user is not logged in the user is redirected to the Login page. 
* Verdict: Code functions as intended.

#### Register Link

* Expected Outcome: If the site user is not logged in, the Register Link will be displayed in the Navigation Bar. When clicked, the user should be redirected to Register account page. 
* Test: Enter the site as a user not logged in, then click Register link. 
* Result: When not logged in the Register link is visible, when clicked the user is redirected to Register account page. 
* Verdict: Code functions as intended.

#### Login Link

* Expected Outcome: If the site user is not logged in, the Login Link will be displayed in the Navigation Bar. When clicked, the user should be redirected to Login page. 
* Test: Enter the site as a user not logged in, then click Login link.
* Result: When not logged in the Login link is visible, when clicked the user is redirected to Login page.
* Verdict: Code functions as intended.

#### Logout Link

* Expected Outcome: If the site user is logged in, the Logout Link will be displayed in the Navigation Bar. When clicked, the user should be redirected to a Logout page to confirm they wish to log out. 
* Test: When logged in, click the Logout Link. 
* Result: When logged in the Logout link is visible, when clicked the user is redirected to Logout page. 
* Verdict: Code functions as intended.

### Footer

#### Footer

* Expected Outcome: The footer should be visible on all pages of the site and always be placed on the bottom of the page. 
* Test: Visit every page of the site to check if footer is visible. 
* Result: The footer is visible on every page of the site. 
* Verdict: Code functions as intended.

#### Footer Links

* Expected Outcome: The icons for social media in the footer are supposed to be opened up in new tabs when clicked, for better UX. 
* Test: Click the social media icons in footer. 
* Result: When clicking the icons the social media is opened up in a new tab. 
* Verdict: Code functions as intended.

### Welcome Text

#### Welcome Text - not logged in

* Expected Outcome: If user is not logged in, a welcome text with clickable links to Login/Register account should be displayed on the home page below the welcome image. 
* Test: Enter the site when not logged in. 
* Result: When entering the site as a user not logged in, a welcome text with fully functional and easily viewed clickable links is displayed. 
* Verdict: Code functions as intended.

#### Welcome Text -logged in

* Expected Outcome: If user is logged in, a welcome text displaying the users username should be displayed on the home page. 
* Test: Enter the site when logged in. 
* Result: When entering the site as a logged in user, a welcome text displaying the correct username is displayed. 
* Verdict: Code functions as intended.

### Recipe List

#### Recipe Overview

* Expected Outcome: When entering the site a list of recipes are supposed to be displayed. The list should present a preview image of each recipe with some basic information including the recipe name and tag line. 
* Test: Enter the site to check if recipes are displayed. 
* Result: When entering the site a list of recipes are presented. Each recipe cards presents a preview of an image, author, title, excerpt (if available), created date and number of likes. 
* Verdict: Code functions as intended.

#### Page Pagination

* Expected Outcome: To make the site more user friendly there should be a maximum of 6 recipes displayed at once. When there are 6 recipes on the page it should paginate and the user should be able to click the 'Next' buttin at the bottom to get to the next page. 
* Test: Check if page pagination is activated if there are more than 6 recipes on the site by adding a larger number of recipes. 
* Result: The seventh recipe that was added to the site was displayed on a second page, visible if the next button was clicked. 
* Verdict: Code functions as intended.

* Expected Outcome: When a specific recipe is clicked the recipe should open on a recipe detail page. On this page you can see an image, title, excerpt (if available), author, updated on, ingredients list, instructions and created on. 
* Test: Click a recipe to check that it opens up and reveals all information. 
* Result: When a recipe is clicked it opens up and reveals information, but date and time it was crated on was not visible. 
* Verdict: Code functions as intended but the date of creation was not visible 
* Solution: Add correction to error to recipe detail template. 
* Test 2: Click a recipe to check that it opens up and reveals all information, including date created. 
* Result 2: When a recipe is clicked it opens up and reveals all available information, including cooking time. 
* Verdict: Code now functions as intended.

#### Likes

* Expected Outcome: When viewing a recipe in full number of likes is supposed to be displayed and if the user is logged in the ability to like/unlike should be available. 
* Test: Open a recipe to see if likes are visible and check that the heart icon is clickable and generates a like. 
* Result: Number of likes are displayed and if the user is logged in the heart is clickable and generates another like. 
* Verdict: Code functions as intended.

#### View Comments

* Expected Outcome: When viewing a recipe in full all comments are supposed to be displayed showing the oldest one first. 
* Test: Open a recipe to see if comments are available to all users and that they are displayed oldest first. 
* Result: Comments are displayed to all users, logged in or not but the name of the user that commented was not present.
* Solution: Fix typo error in comments model
* Test 2: Open a recipe to see if comments are available to all users and that they are displayed oldest first. 
* Verdict: Code functions as intended.

### About Page

* Expected Outcome: When visiting the About page the user should be presented with some information regarding the site and it's ethos. 
* Test: Visit About page to view content. 
* Result: When visiting the About page the content of the site is displayed in a neat and explanatory way with eye cathcing images. For better user experience when viewed on smaller screens the images on the page are hidden since they serve a design purpose only. 
* Verdict: Code functions as intended.

### Add Recipe


* Expected Outcome: A logged in user is supposed to be able to add recipes to the site. 
* Test: As logged in user add a new recipe, trying to leave fields blank and filling out all. 
* Result: When leaving one or more of the required fields blank the user is encouraged to fill out the form completely. If that requiry is met the recipe is uploaded and the user is redirected to the home page. 
* Verdict: Code functions as intended.

### Placeholder image

* Expected Outcome: If the user does not choose to upload an image for their recipe a placeholder image of food should be displayed.
* Test: Add recipe without image. 
* Result: When adding a recipe but not uploading an image, the placeholder image will be displayed. 
* Verdict: Code functions as intended.

### Register New Account

* Expected Outcome: As a site user you should be able to create an account to be able to interact with the site. The username has to be unique and entering an email address is optional. 
* Test: Create new account with unique username, create new account with already existing username, create new account with and without email address. 
* Result: If the new account has a unique username the account is created, regardless whether an email address is entered or not. When trying to create a new account with an existing username, the user is encouraged to choose a unique username since it already exists. When the account is registered the user is logged in and is notified by an alert. 
* Verdict: Code functions as intended.


### Login

* Expected Outcome: As a registered site user you should be able to log in to your account to be able to interact with the site. If you wish your login credentials can also be saved on your computer ensuring you do not have to fill them each time you visit the site. 
* Test: Check Login functionality as registered user. 
* Result: When entering valid login credentials the user is logged in and redirected to the home page and an alert notifies the user that they are logged in. 
* Verdict: Code functions as intended.

### Logout

* Expected Outcome: As a registered and logged in user you should be able to log out of the site. 
* Test: Check Logout functionality as logged in user. 
* Result: When clicking Logout the user is redirected to Logout page and asked to confirm that they wish to log out. When Log Out button is clicked the user is logged out and redirected to home page. 
* Verdict: Code functions as intended.

## Automated Testing

### Code Validation

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the HTML and CSS code used. The [PEP8 Python Validator](http://pep8online.com/) was used to validate the Python code. 

#### Results:

* HTML Validation - all pages clear

* CCS Validation - page clear 

* Python Validation - all pages clear

Files tested: 
*Blog*
* admin.py
* apps.py
* forms.py
* models.py
* urls.py
* views.py
*Eatopia*
* setting.py
* urls.py

### Browser Validation

The site has been tested using the following browsers:

* Chrome
* Firefox
* Edge
* Safari


## **Bugs**

* **Bug** - When uploading a recipe I was recieving a TypeError from my views.py file. 

  **Solution** - After discovering that it was a problem occuring during render, I done some research and discovered that the version of Summernote i had installed went out of date. 

* **Bug** - Recieving a NoReverseMatch error when uploading a recipe. 

  **Solution** - After working through my code and adding a recipe in the admin panel. I discovered that whilst adding a recipe through the 'Add Recipe' page, slugs were not been allocated and this was causing the error. I searched on StackOverflow and found a solution and installed Slugify. 

* **Bug** - Recieved a TemplateDoesNotExist error when trying to get my forms to function. 

  **Solution** - After troublehooting and being unable to determine the cause, I reached out to the Tutor team and Rebecca informed me that there was an issue with Crispy Forms 2.0. I then downgraded to a previous version of Crispy Forms and this resolved the error.  

* **Known Bug** - If a user creates a recipe that has the same name of another recipe then an error will be thrown. This is because the slug is generated from the recipe title. To fix this in the future I will research how to make a user create a unique recipe title and in doing so have a uniwue slug, this would prevent the error from occuring.


## **Technology Used**

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
     - Used to implement the Summernote feature that allowed the user to add styling to the recipe in the form.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")
     - Used to implement Django functionality, including building models, forms and views for the app.

### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website")
    - Django was used to build the models, forms and views of the app, and was the backbone of this project.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes, but also other styling such as buttons etc.
- [Cloudinary](https://cloudinary.com/ "Link to Cloudinary page")
     - Cloudinary was used as free cloud storage for images uploaded to the site through the recipe forms.
- [Summernote](https://summernote.org "Link to Summernote page")
     - Summernote was used to allow users to add styling when adding a recipe to the site. This is particularly useful for using bullet points for ingredients or numbering the steps for the recipe.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to the Crispy Forms documentation")
    - Crispy Forms was used to style the add and edit recipe forms, allowing more than one field to occupy a line on the form.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts were used to import the fonts "Roboto" and "Lato" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup imagery to be used.
- [Balsamiq Wireframes](https://balsamiq.com/learn/articles/what-are-wireframes/ "Link to Balsamiq Wireframes")
     - Balsamiq Wireframes was used to create the wireframes for the project.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the ElephantSQL postgres database:
    - Create an Instance in ElephantSQL.
    - Copy the URL and paste it into env.py.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary:
    - Create three directories in the main directory; media, static and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi

5. Deploy to Heroku:
     - Link GitHub repository and Deploy Branch. 


## Credits

### Media

All food images were got from [Pexels](https://www.pexels.com/)

### Code

* [Crispy Forms Docs](https://django-crispy-forms.readthedocs.io/en/latest/)
* [Summernote Github Docs](https://github.com/summernote)
* [Bootstrap](https://getbootstrap.com/)
* [Django Docs](https://docs.djangoproject.com/en/4.0/)
* [w3 Schools](https://www.w3schools.com/)
* [Stack Overflow](https://stackoverflow.com/)

### Acknowledgements

* The Code Institute Tutor Team for the invaluable help and advice. 
* My Mentor Richard for all his expertise in guiding me through this project. 
* Everyone on Slack that helped whenever a question was asked. 







    
    







