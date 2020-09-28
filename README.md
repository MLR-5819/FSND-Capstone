# FSND Capstone
 Udacity Project 5

TODO:
Create DB #done
    Add data to DB #done
Define Models #done
Define API endpoints/Create simple frontend #
Define Auth0 #
test locally (test.py) #done
Write readme doc
deploy to heroku #done
test deployed app # done
submit!

https://udacity-fsnd-tot.herokuapp.com/ 

user@thisorthat.com - TestUserP@ssw0rd
#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtoX3drdVlWNGwzT1FIX2pvaGZ6MSJ9.eyJpc3MiOiJodHRwczovL2Rldi1tcm9zZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3MGQxZjBhNTExZmUwMDZiNzhmZDQwIiwiYXVkIjoidG90IiwiaWF0IjoxNjAxMjU0NTc0LCJleHAiOjE2MDEyNjE3NzQsImF6cCI6ImtZV0JvdjV0eWlZazkwRTZvc0dXaHRGNUlLeENmS3pOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJwYXRjaDplbnRyeSIsInBvc3Q6ZW50cnkiXX0.VKeXZrDQ8rZsmDkJUhaEqR7F1ETBrvbbp_9EUvtR7q3OQJptgSrLzwzSGVeDrgSAYOPI0Esw3qiIkw-0UaVNYBwV2J1l2L2I5AMp2imfMc0E8KPJa3YxCWKV8Ji8-GOGdngyQm-Cv4LwKR4GZiCTbQocISNLuwzN8EjhtylKJkE_6hwu2eMecMxB3rMxXrPMUpyq_IpEDdxu2UKOrKfRrLWvdkgxdR5Z9T0gO55DSTWCYnTbemdQnQfCgIxBZBbhZNGBeF_5o8T21cdyR2c1yXb0bx22YoHxSr5B_wNuIvsk2UgPCCQvYjM6Q5tC7_adubTBZGHc7K8wCJUJc3A0LQ&expires_in=7200&token_type=Bearer

admin@thisorthat.com - TestAdminP@ssw0rd
#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtoX3drdVlWNGwzT1FIX2pvaGZ6MSJ9.eyJpc3MiOiJodHRwczovL2Rldi1tcm9zZS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3MGQyYWI2MzAwMjQwMDcxOTM4ZmY1IiwiYXVkIjoidG90IiwiaWF0IjoxNjAxMjU0NDk5LCJleHAiOjE2MDEyNjE2OTksImF6cCI6ImtZV0JvdjV0eWlZazkwRTZvc0dXaHRGNUlLeENmS3pOIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZW50cnkiLCJwYXRjaDplbnRyeSIsInBvc3Q6ZW50cnkiXX0.QMXDam7eiZlmaWpKyT6HZVgq9EXVR3mLmxF_xutmvikG6b8DJg_3_yHqamrLsBYsZel2PQlwG8WgXkXh3z5NkzrPyp2EvJ1dYWqK3ZSVzpKo5dv7A-16oxci30UR_1gpOCDTLUYhkCVtuxIvrWi33G7xIIMmB-0aJSujWynni_ojGO_4WPvl2XDsTG6We9yy8RP8KcOyqhUdJ6-Bgt5p-NFmuEq1epk063aPRZzgRf8tzwXu-Xu1AjOXqeKtVCRaCoDwSZ6KTUXyy41ETvoosiSWKcl8CdIRl_dgcHEAVA99gWrNdzc3YfSC7DRtVcKBdrCX7OPwp0Ya7PkPLbt3BQ&expires_in=7200&token_type=Bearer

start of README.md content below
################################

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
* Other requirements listed in requirements.txt **update file

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
| GET | / | Welcome page

