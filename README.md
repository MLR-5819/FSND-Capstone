# This or That API
## Udacity Full Stack Nanodegree Capstone Project

![Image of ToTLogo](https://udacity-fsnd-tot.herokuapp.com/static/img/thisorthat.png)

### Introduction

 This or That is a entertainment site that lets you view images from all different categorgies, while allowing to vote for your favorite picture in a This or That battle. This site lets you add your favorite pictures for many different categories to gain wider audience exposure for your social media. Many more features to come.

### Overview

This app is nearly complete. However, it is missing a few things. The 'Play' and 'Social' features have not been implemented. For now anyone can add their favorite pictures to grow the database. To make updates to your submission you must sign up. To request deletion of your submission, please email our Administrator.  *App only created for this project*

## Tech Stack

Our tech stack will include:

* **Heroku** - App Deployment
* **Auth0** - Authorization management
* **SQLAlchemy ORM** - ORM library
* **PostgreSQL** - database
* **Python3** and **Flask** - server language and server framework
* **Flask-Migrate** - schema migrations management
* **HTML** & **CSS** - website's frontend
* Other requirements listed in **requirements.txt**

## Live Application & Users

| **Link** | https://udacity-fsnd-tot.herokuapp.com/ |
|----------|-----------------------------------------|
| **Users** | **Password** |
| admin@thisorthat.com | TestAdminP@ssw0rd |
| user@thisorthat.com | TestUserP@ssw0rd |

## Auth0 Roles/Permissions for authentication
| User | Role | Permissions |
|------|------|-------------|
| user@thisorthat.com | User | post:entry <br> patch:entry |
| admin@thisorthat.com | Admin | post:entry <br> patch:entry <br> delete:entry |

## Main Files: Project Structure

  ```sh
  ├── README.md
  ├── app.py *** the main driver of the app.
        "python app.py" to run after installing dependences
  ├── auth.py
  ├── forms.py
  ├── manage.py
  ├── models.py
  ├── test_app.py  
  ├── Procfile
  ├── setup.sh
  ├── requirements.txt *** The dependencies we need to   
        install with "pip install -r requirements.txt"
  ├── _pycache_     
  ├── migrations
  ├── static
  │   ├── css 
  │   └── img
  └── templates
  ```

## Development Setup

[Install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask)

  ```
  $ cd ~
  $ sudo pip install Flask
  ```

To start/run the local dev server:

1. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

2. Run the development server:
  ```
  $ export FLASK_APP=app.py
  $ export FLASK_ENV=development
  $ python app.py
  ```

4. Navigate to page [http://localhost:8080](http://localhost:8080)

## Endpoints

### The following are the available API endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome page |
| GET | /categories | Render 'categories.html' getting all categories and displaying all entries. |
| GET | /categories/**(id)** | Render 'show_category.html' getting 1 category and displaying all entries under that category. |
| GET | /entries/**(id)** | Render 'show_entry.html' showing 1 entry's details. |
| GET, POST | /entries/add | GET displays the form rendered on 'add_entry.html', POST adds the new entry to the database and redirects to 'categories.html' |
| GET, POST, PATCH | /entries/**(id)**/update | GET displays the form rendered on 'update_entry.html', POST/PATCH updates the entry to the database and redirects to 'categories.html'. **Must be registered and assigned the *'User'* role.** |
| GET, DELETE | /entries/**(id)**/delete | Deletes entry and redirects to 'categories.html'. **Must be registered and assigned the *'Admin'* role.** |
| GET | /play | Render 'play.html'. Function to be developed. |
| GET | /logout | Redirects to Auth0 logout link.|

## Sample Data Returned
### GET '/categories' - render_template returned. 
#### 'api/categories' returns json data for testing.
```
curl http://127.0.0.1:8080/api/categories 
```
```
 "categories": [
    {
      "id": 6,
      "type": "Cars"
    },
    {
      "id": 2,
      "type": "Cats"
    },
    {
      "id": 3,
      "type": "Dogs"
    },
    {
      "id": 1,
      "type": "Food"
    },
    {
      "id": 5,
      "type": "Places"
    },
    {
      "id": 4,
      "type": "Tattoos"
    }
  ],
  "entries": [
    {
        "id": 5,
        "image": "https://images-na.ssl-images-amazon.com/exampleURL.jpg",
        "name": "Classic Corvette",
        "votes": 20
    },
```
### Sample error returned.
```
curl http://127.0.0.1:8080/api/categories/22
```
```
{
  "error": 404,
  "message": "Resource Not Found",
  "success": false
}
```
## Unittest Testing
```
python test_app.py
```

# :+1: