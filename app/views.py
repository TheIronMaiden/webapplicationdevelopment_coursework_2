from app import app, models, forms, db
from flask_wtf import Form
from flask import Flask, request, render_template, redirect, url_for, flash
from .forms import LoginForm
from .forms import UserForm
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from .forms import UpdateProfileForm

@app.route('/')
@app.route('/index')
# @login_required
def index():
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day today!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("BINGO! current user:", current_user)
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return(redirect(next_page))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return(redirect(url_for('index')))

@app.route('/createlogin', methods=['GET', 'POST'])
def createlogin():

    form = UserForm()
    if form.validate_on_submit():
        print(form)
        print(form.username.data)
        user = User(nickname=form.nickname.data, username=form.username.data)
        print(user.nickname)
        print(user.username)
        user.set_password(form.password.data)
        print(user.password)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('createlogin.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

@app.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        current_user.password = form.password.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
        form.password.data = current_user.password
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)
