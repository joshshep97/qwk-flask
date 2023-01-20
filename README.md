# qwk-flask
A flask quick-start module to get building immediately 

## File tree
📦core 
 ┣ 📂main
 ┃ ┣ 📜routes.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┣ 📜main.css
 ┃ ┗ 📜script.js
 ┣ 📂templates
 ┃ ┣ 📜base.html
 ┃ ┗ 📜index.html
 ┣ 📜models.py
 ┗ 📜__init__.py
┣ app.py 

## Includes
- run file (app.py)
- templates folder - w/ base and index.html
- main blueprint for your app - initialized 
- static folder - for CSS, JS, IMG's
- models folder 
- __init__.py where the main factory function (create_app()) exists

## To do
- git clone https://github.com/Optimized-Coder/qwk-flask.git
- add .env file
    - $ git touch .env
    - set my_secret_key to your secret key

Then you're ready to start building your app with more routes and styles! 

P.S. app is set to port(5050) as I was already running :5000 on my local server at the time of building
