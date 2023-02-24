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







    
    







