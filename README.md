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

## How To DIY

### Set up your environment
In the root folder of your application, run:
```
root
$ py -m venv env
```
This will create a new virtual environment so you can access environment variables as well as keep order of your depenenies.

Then:
```
root
$ source env/Scripts/activate
```
**Note: if your are using Mac or Linux then substitute "Scripts" for "bin"**



Next, you will need to create a new file called 'app.py'. You can call it what you want but this is conventional

```
--> app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True, port=5050)
```

Then, if you return to your git bash terminal, and use the command:

```
$ python app.py
```

your application will run at port on your localhost server. Type either:
- 127.0.0.1:5050
- localhost:5000

into your browser and, if all is working, you should see your first application.  

For more information visit [the documentation](https://flask.palletsprojects.com/en/2.2.x/)

---

You're ready to start building your app with more routes and styles! 

P.S. app is set to port(5050) as I was already running :5000 on my local server at the time of building


