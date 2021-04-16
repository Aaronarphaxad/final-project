# CS50 Final Project
 

### Introduction

Rookie Hub is a flask web app built by Aaron Omale. Rookie Hub is a website that generates quizzes for rookie developers to test their knowledge on HTML, CSS, and javascript. It was built as final project for Harvard's introduction to computer science course (CS50). 


### Technologies used

Flask, Javascript, Python, HTML, Cascading Style Sheets (CSS).

### Features

- This project has a content management system which can be used to automatically add questions to the      questions bank using a form
- Dynamic grading system
- Dark mode toggle
- Google Recaptcha

### Challenges faced

This project took me over 3 weeks to complete because I wanted to do something beyond my comfort zone. So I had to dive deeper into learning more of python programming language to be able to utilize some methods and functions which helped me with backend tools.
I also had some trouble with the overall design choices and fonts to use. I wanted to make it look like a fun website. So I did some research on that too.
The major challenge I faced was deploying the app to Heroku. I learnt a LOT!!!

### Code break down

- Most of the heavy lifting happened in the app.py file. Which contains the routes, table declararion using SQLAlchemy, and other configurations like recaptcha.
- Templates contains all the html files rendered to the client side, including the layout (default) page.
- Static folder contains all the Javascript files, CSS files, and images.
- Helpers.py contain all the functions I used to make my code a little cleaner and readable.
- formParser.py contain helper functions for the content management.
- Requirements.txt contains all the technologies installed mostly using pip. It was automatically updated using 
```
pip install freeze > requirements.txt
```
- During developement I used sqlite as my database, but I had to switch to postgre SQL during deployment, because heroku does not allow sqlite. I did that by changing the SQLAlchemy DATABASE URI to: 
```
postgresql:///"link provided"
```
- Procfile: This tells heroku dynos what to do with the app. 


### Credits

I learnt a lot from so many blogs and youtube videos. I cannot remember all. But I want to mention stack overflow, Medium, W3Schools, and other websites with free educational resources that change lives.
I also wang to thank my friend Obafemi Joseph, for always explaining things to me whenever I'm stuck, and also fixing and debugging my codes.

### License 

Copyright (c) 2021 Aaron Arphaxad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. 
