import os

import requests

from flask import Flask, render_template, url_for, request, flash, redirect, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"Rq45z\n\xec]/'

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template('index.html')

#Review Form
class TextField(Form):
    review = StringField('Review', [validators.Length(min=1, max=300)])

#Registration forms - User infos
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():

    # Registration form
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # Sending input data to DB.
        db.execute("INSERT INTO users (name,email,username,password) VALUES (:name, :email, :username , :password)",
                   {"name": name, "email": email, "username": username, "password": password})

        # Commit to Database
        db.commit()
        return render_template('success.html')
    return render_template('register.html', form=form)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_user = request.form['password']
        # Get user by username

        result = db.execute("SELECT * FROM users WHERE username = :username", {"username": username}).fetchone()
        #Getting id from Current User
        if result is None:
            return render_template("error.html", message="No users found.")
        else:
            # Get stored hash
            password = result['password']

            # Compare Passwords
            if sha256_crypt.verify(password_user, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username
                flash('You are now logged in' , 'success')
                return render_template('index.html')
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)

    else:
        return render_template('login.html')

#Logout
@app.route('/logout')
def logout():

    #To clear the user id
    session.clear()

    # Redirect user to the login page
    return redirect(url_for('login'))


@app.route('/search', methods=['GET'])
def search():
    book = "%" + request.args.get("book") + "%"
    book = book.title()
    books = db.execute("SELECT * FROM books WHERE (isbn) LIKE :book OR (title) LIKE :book OR (author) LIKE :book", {"book": book}).fetchall()
    books_len = len(books)
    if books_len == 0:
        return render_template("error.html", message = "No books found.")
    else:
        return render_template("results.html", books=books)


# Single page book - With all info 
@app.route("/book/<string:book_isbn>", methods=['GET','POST'])
def book(book_isbn):
    '''Fecthing single book by isbn'''
    if request.method == "POST":

        currentUser = session["username"]
        # Fetch form data
        rating = request.form.get("rating")
        comment = request.form.get("comment")

        # Book_id by ISBN
        row = db.execute("SELECT id FROM books WHERE isbn= :isbn",{"isbn": book_isbn})

        #Save as a variable
        bookId = row.fetchone()
        bookId = bookId[0]
        # Putting as a Integer to save on the database
        rating = int(rating)

        #Checking if the review has been already submitted by the user logged in.
        review_check = db.execute("SELECT * FROM reviews where username= :username AND book_id = :book_id",
                        {"username":currentUser,
                         "book_id":bookId})
        if review_check.rowcount == 1:
            flash("Review already submitted for this book", 'danger')
            return redirect("/book/"+book_isbn)


        db.execute("INSERT INTO reviews (book_id, username, comment, rating) VALUES \
                       (:book_id, :username, :comment, :rating)",
                       {"book_id": bookId,
                        "username": currentUser,
                        "comment":comment,
                        "rating":rating})
        db.commit()

        return redirect("/book/"+ book_isbn)
    else:

        book = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": book_isbn}).fetchone()

    # Set up API - Goodreads : KEY = "dCb5gYyxdpbZIEBAJh9fg"
        res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": "dCb5gYyxdpbZIEBAJh9fg", "isbns": book_isbn})
    #Data from Json API.
        data = res.json()
        avgrating = data["books"][0]["average_rating"]
        rating_work = data["books"][0]["work_ratings_count"]
    #Fetching book reviews

        return render_template("book.html", book=book, avgrating=avgrating, rating_work=rating_work)




if __name__ == '__main__':
    app.run(debug=True)