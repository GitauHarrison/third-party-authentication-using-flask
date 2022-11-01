# Third Party Authentication in Flask

![Third Party Authentication](/app/static/images/flask_oauth.gif)

### Overview

The use of third party apps to assist in login is fairly common. It improves a user's experience whenever they want to access content that is protected.

### Tools Used
* Rauth 
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
* [Flask third party auth](https://flask-third-party-auth.herokuapp.com/) - Heroku
* [Flask Third Parth Auth](https://third-party-auth.onrender.com) - Render

### Contributors
* [Gitau Harrison](https://github.com/GitauHarrison)

### Testing Deployed App

* Click on either _LOGIN WITH FACEBOOK_ or _LOGIN WITH TWITTER_ buttons
* Enter your account details upon request
* You should be able to log in

### Testing Locally

You will need:

* [Facebook app account](https://developer.facebook.com/)
* [Twitter developer account](https://apps.twitter.com/)

Learn how to create a Facebook and a Twitter app in this [ third party authentication guide](https://github.com/GitauHarrison/notes/blob/master/two_factor_authentication/third_party_auth.md). From this guide you will  learn how to generate your Facebook and Twitter apps' _API Keys_ and _Secret_ID_. You will need them to run this application locally.

#### Additional Notes on Twitter Developer API

Twitter API working you need "Elevated" Access Level

Screenshot from below Page: 
https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve

Additionally you need to add the below URL to your *Callback URI / Redirect URL* settings in Twitter developer API
```http://127.0.0.1:5000/callback/twitter```

<img width="617" alt="image" src="https://user-images.githubusercontent.com/5732092/177808540-18c5ea45-fe3d-4753-b562-facf34af23c8.png">


<img width="909" alt="image" src="https://user-images.githubusercontent.com/5732092/177788365-23bd0dc8-a2bb-4f3e-b62d-abfbe6fab41b.png">


If you have only "Essential" Twitter API Access - you will get the below error message in response.

```
127.0.0.1 - - [07/Jul/2022 03:37:32] "GET /authorize/twitter HTTP/1.1" 302 -
{'errors': [{'message': 'You currently have Essential access which includes access to Twitter API v2 endpoints only. If you need access to this endpoint, you’ll need to apply for Elevated access via the Developer Portal. You can learn more here: https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api#v2-access-leve', 'code': 453}]}
social_id:twitter$None
```

To test this application, first 

1. Clone it:

```python
$ git clone git@github.com:GitauHarrison/third-party-authentication-using-flask.git
```

2. Create and activate your virtual environment:

```python
$ mkvirtualenv flask_auth_test # I am using virtualenvwrapper
```

3. Install necessary dependancies as seen in `requirements.txt`:

```python
(flask_auth_test)$ pip3 install -r requirements.txt
```

4. Run the application:
```python
(flask_auth_test)$ flask run
```

5. Before you can run your server, remember to create a `.env` file following the guidance seen in the `.env-template`. Create a `.env` file in the root directory:

```python
(flask_auth_test)$ touch .env
```

6. Update the `.env` file with all the necessary details. Here is a sample:

```python
TWITTER_ID=
TWITTER_SECRET=
FACEBOOK_ID=
FACEBOOK_SECRET=
```

7. Run flask server:

```python
(flask_auth_test)$ flask run
```

Once your application is running, you can access your localhost on http://127.0.0.1:5000/. I have not used `ngrok`. If you wish to do so, to provision temporary public URLs that will allow access to your application, learn how you can set it up [here](https://gitauharrison-blog.herokuapp.com/ngrok).

With the application running:

* Click on either social login buttons
* Authorize your account to sign you up
* You should be able to see the home page

### References

1. If you do not know how to make a flask application, learn how to do that [here](https://github.com/GitauHarrison/notes/blob/master/web_development/personal_blog/personal_blog.md).

2. This application makes use of `ngrok`. Learn how to incorporate it in your flask app [here](https://github.com/GitauHarrison/notes/blob/master/localhost_testing.md).

3. If you would like to know how to know how to integrate social logins (rather than simply running this application), [read more here](https://github.com/GitauHarrison/notes/blob/master/two_factor_authentication/third_party_auth.md).