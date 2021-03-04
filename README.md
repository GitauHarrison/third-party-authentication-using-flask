# Third Party Authentication in Flask

![Third Party Authentication](/app/static/images/flask_auth.png)

### Overview

The use of third party apps to assist in login is fairly common. It improves a user's experience whenever they want to access content that is protected.

### Tools Used
* Flask framework
* Python 3 for programming
* SQLite database
* Flask-Bootstrap for crossplatform responsiveness
* Flask-WTF for web form creation
* Flask-Migrate for database management
* Flask-Mail to handle password reset requests
* Twitter API
* FaceBook API
* Heroku for deployment

### Features
* User authentication
* Password Reset
* Message flashing for improved user feedback
* Error handling and useful redirects
* Social Logins

### Deployed Application
* [Flask third party auth](https://flask-third-party-auth.herokuapp.com/)

### Contributors
* [Gitau Harrison](https://github.com/GitauHarrison)

### Testing
To test this application, first clone it:

```python
$ git clone git@github.com:GitauHarrison/third-party-authentication-using-flask.git
```

Create and activate your virtual environment:

```python
$ mkvirtualenv flask_auth_test # I am using virtualenvwrapper
```

Install necessary dependancies as seen in `requirements.txt`:

```python
(flask_auth_test)$ pip3 install -r requirements.txt
```

Run the application:
```python
(flask_auth_test)$ flask run
```