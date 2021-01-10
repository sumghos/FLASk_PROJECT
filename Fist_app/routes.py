from flask import render_template, url_for, flash, redirect
from Fist_app import app,db,bcrypt
from Fist_app.form import RegistrationForm, LoginForm
from Fist_app.models import User, Post


posts = [
    {
        'author': 'sumit Ghosh',
        'title': 'Blog posts about AI',
        'content': 'This all about the AI and not sure about it ',
        'date_posted': 'MAY 24,2020'
    },
    {
        'author': 'Dipanjan Halder',
        'title': 'Blog posts about Devops',
        'content': 'This all about the Devops and not sure about it ',
        'date_posted': 'MAY 25,2020'

    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
