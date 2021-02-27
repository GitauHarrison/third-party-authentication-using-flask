# Third Party Authentication in Flask

![Third Party Authentication](/app/static/images/flask_auth.png)

The use of third party apps to assist in login is fairly common. It improves a user's experience whenever they want to access content that is protected.

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