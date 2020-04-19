# Project 1 - Book Reviewer 

A website to rate, reviews and infos about books matching with GoodReads.com IPA database for 
CS50W - Web Programming with Python and JavaScript

## Usage

- Register. 
- Login. 
- Search for a book using any of two search bars.
- Choose your book to look infos, reviews and to give your own. 

## Built With

* [Python](https://docs.python.org/3/) - The main language used.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The framework used. 
* [Heroku](https://dashboard.heroku.com/login) - Used for database and deployment.
* [PostgreSQL](https://www.postgresql.org/docs/) - DB System.


### Prerequisites

Python 3.6 or higher installed in your machine. 


### Setting up your environemt. 

```
#Download or clone the repository on your machine. 
$ https://github.com/douglasvinicio/cs50w-project1.git

- Line 173 of apllication.py set your Goodreads API key.

Example : Set up API - Goodreads : KEY = "GOODREADS API KEY"
        res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": "GOODREADS API KEY", "isbns": book_isbn})

- In a terminal window, navigate into your project1 directory.

- Run pip3 install -r requirements.txt in your terminal window to make sure that all of the necessary Python packages (Flask and SQLAlchemy, for instance) are installed.

- 

- In your terminal window "FLASK_APP=application.py"; 
- Set the enviroment variable to 1 with "FLASK_DEBUG=1" to activate the automatic reload of the server after changes in your code;
- Set the database variable with : export DATABASE_URL=“(credentials provided by Heroku)“;
- Run "flask run" in your terminal;
- Navigate to the url provided by Flask;
```

