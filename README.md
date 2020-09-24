# CS50W - Web Programming with Python and JavaScript - Project 1 - Book Reviewer 
<!-- header section -->
<p align="center">
  <img  alt="Events Maker  - Logo" src="https://i.ibb.co/wWh80X9/lo-ve.png" height="auto" /><br/>
  <span>Book Reviewer CS50 <b> Python / Flask / PostgreSQL / Jinja2 </b></span><br/>
  <span>A website to rate, review and see info about books working together with goodreads.com API.<b> And also works as a API itself.</b><span><br>
  <span>Running on <b>Safari, Chrome and Firefox </b>. </span><br/>
</p>

<!-- show case/gif section -->
<p align="center">
    <img alt="Events Maker - Chat " height="300" src="https://media.giphy.com/media/ihYtw7oXgnkErkZ3Im/giphy.gif" />
    <img alt="Events Maker - Creating user and Channel " height="300" src="https://media.giphy.com/media/fxT3gcB35y6m7ufAPE/giphy.gif" />
  </a>
</p>



### Project Objectives and Requirements - https://docs.cs50.net/web/2020/x/projects/1/project1.html

### Project deployed at Heroku - https://cs50bookreviewer.herokuapp.com

## Website Functionalities 

- Search for books
- Reviews
- Rating
- API
- goodreads.com data connected via API
- Book covers

## Built With

* [Python](https://docs.python.org/3/) - The main language used.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The framework used. 
* [Heroku](https://dashboard.heroku.com/login) - Used for database and deployment.
* [PostgreSQL](https://www.postgresql.org/docs/) - DB System.

## Obejctive

A website to get informations about books, using its own database with more than 5000 titles giving the user the option to 
give its opinion and rate books. Also using the API from "goodreads.com to retrive information about the book selected.


### Let's run the app.
#### Download or clone the repository on your machine. 
$ https://github.com/douglasvinicio/cs50w-project1.git


##### Go to the folder application.
##### Make sure you install a copy of Python 3.6 or higher.
##### Make sure you have pip installed too. If not run this command : 
$ python get-pip.py
##### Install all dependencies :
$ pip install -r requirements.txt
##### Create a virtualenv :
$ export FLASK_APP=application.py
##### Set the DATABASE URL :
$ export DATABASE_URL=" link provided by heroku postgres add-on "
##### Run
$ flask run
##### Go to 127.0.0.1:5000 on your web browser.

##### To use the API function just type in your navigator the isbn number right after api/ : 
- http://127.0.0.1:5000/api/ "ISBN" 

### Usage

- Register. 
- Login. 
- Search for a book using any of two search bars.
- Choose your book to look infos, reviews and to give your own. 




## Team

<table>
  <tr>
    <td align="center"><a href="https://www.linkedin.com/in/douglasvinicio/"><img src="https://trello-attachments.s3.amazonaws.com/5eab8674a86a907c46dbf222/128x128/72740d1400b95b82bea9ea85b7c1b592/douglasvinicio.png" width="100px;" alt="Douglas Vinicio"/><br /><sub><b>Douglas Vinicio</b></sub></a><br /><a href="https://github.com/douglasvinicio"title="Code">💻</a></td>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->
