# Jenkins App
This app is used to get a list of jobs and their status from a given jenkins instance using Jenkins API.

Getting Started
---------------
The steps below will get you up and running with a local development environment. We assume you have the following installed:

-   pip
-   virtualenv

Installation
------------
Clone the repository, then install all requirement
> $ pip install -r requirements.txt
> $ python manage.py migrate

Running Django App
------------------
Run the django app:
> $ python manage.py runserver

Then access from browser to [localhost:8000](http://localhost:8000/)
For admin page, you can use username/password as **admin**/**admin**

Running Python Script
---------------------
This python script is used to get a list of jobs and their status from a given jenkins instance using Jenkins API. 
> $ python jenkins_sync.py

After execute this script, the job and status will save in same database with django app. You can see the data via admin page in django app.

The Jenkins, I have installed in my test server `http://128.199.185.100:8080/`, you can login use user/password : **jenkins**/**jenkins**
