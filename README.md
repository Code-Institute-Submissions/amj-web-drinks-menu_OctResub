# The Drinks Menu

The Drinks Menu is a place for visitors to find and share cocktail recipes. Users are able to register an account, then share and mange their own cocktail recipes. 
## Installation

Here is a [link](https://drinks-menu.herokuapp.com/) to deployed app

## Project Overview

The Drinks Menu is built using **Pyhton, PostGresSQL, Bootstrap, Javascript and Django** the images are being managed by **Cloudinary.** 

## User Stories
**First-Time Visitor Goals - As a first-time user, who has not created an account, I want to be able to:**
* Understand what the purpose of the application is and how to use it.  
* View the recipes
* Create an account

**Registered User Goals - As a registered user I want to be able to:**
* Create, Edit and delete my own cocktail recipes
* View the recipes
* Create an account
* Upload an image of my cocktail
* Comment on other user's recipes

**Site Admin Goals - As an administrator, I want to be able to:**
* Create, Edit and delete my own cocktail recipes
* Search and view specific recipes
* Manage and authenticate user's posts and comments

## Functionality Requirments 
* Full CRUD functionality
* Intuitive navigation
* Responsive to different screen sizes [http://www.responsinator.com/?url=https%3A%2F%2F8000-amjweb-drinksmenu-kaemokxwq2e.ws-us65.gitpod.io%2F]

## Errors
* errors
* errors
* errors

## Testing
**HTML**

**CSS**
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
    </a>
</p>
            

**JS**

**Python**

**Lighthouse**

**Responsive Design**

## Documentation used

**Django**
- https://docs.djangoproject.com/en/4.1/

**Create Post**
-   https://stackoverflow.com/questions/6253611/how-to-get-the-id-of-a-just-created-record-in-django

**Update Post**

-   https://www.geeksforgeeks.org/update-view-function-based-views-django/
-   https://docs.djangoproject.com/en/4.1/topics/class-based-views/intro/

**Image Upload to Cloudinary**

-   https://docs.djangoproject.com/en/4.1/topics/http/file-uploads/
-   https://cloudinary.com/documentation/django_integration
-   https://cloudinary.com/documentation/django_image_and_video_upload
-   https://stackoverflow.com/questions/33003173/linking-a-cloudinary-image-upload-to-a-django-model-field

**General Fixes**
-   https://stackoverflow.com/questions/4642596/how-do-i-check-whether-this-user-is-anonymous-or-actually-a-user-on-my-system
-   https://stackoverflow.com/questions/57674348/typeerror-post-got-an-unexpected-keyword-argument

**Bootstrap**

**Getting Images same height**

-   https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width

## Thingy

I used unplash to source many of the pictures -https://unsplash.com/

## Fixes and Changes to make in the future

* Change the excerpt to method(how to make the drink) and the contents to ingredients. 
* The Sign Up button on the index page does not show an error when a user who is already logged in clicks on it. 
* The text size changes on the log in page. 
* It is not obvious that The Drinks Menu button will take you to the blog. 
* After signing up the user needs to be redirected straight to the blog. 
* After deleting a post it takes the user to the index page and not the blog. 
