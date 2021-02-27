from app import app
from flask import render_template
from app.forms import Loginform, RegisterForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login')
def login():
    form = Loginform()
    return render_template('login.html', title='Login', form=form)


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title='Register', form=form)
