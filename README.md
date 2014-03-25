django-workshop
===============

This is a workshop conducted at the UPR Bayamon in the first two weeks of April 2014. This project is intended for beginners in Django. In the following their are instructions and guidelines to help you install and understand this project.


Installation
============

## Python

We assume you have python 2.7.* already installed. To check if you have python installed, open a terminal window ( on Windows, CMD ) and type the following or copy & paste:

```
python
```

If you see a prompt and some messages like these:

```
Python 2.7.5 (default, Aug 25 2013, 00:04:04)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

Then you have **python** installed. If you do not see anything like the above, then you can go and install **python** from here.
[https://www.python.org/downloads/](https://www.python.org/downloads/)

## Pip

Once you have **python** installed, you have to install **pip**. You can get **pip** from here. [http://www.pip-installer.org/en/latest/installing.html](http://www.pip-installer.org/en/latest/installing.html)

## Virtualenv
Once you have **pip** installed, you should install **virtualenv**. You can install **virtualenv** by entering this command in the terminal ( CMD ).

```
pip install virtualenv
```

## Cloning the repository

Once that's done. You can clone this repository by using **git**. If you have it installed.

```
git clone https://github.com/Jpadilla1/django-workshop.git
```

Or you can download it from here.
[https://github.com/Jpadilla1/django-workshop/archive/master.zip](https://github.com/Jpadilla1/django-workshop/archive/master.zip)

## Creating a virtual enviroment

Then, in your terminal window ( CMD ), cd ( change directory ) into the folder you have the downloaded and unzipped the project. After that, let's create our **virtual enviroment** by entering the following command.

```
virtualenv venv
```

And activate your enviroment with this command on Ubuntu or Mac.

```
source venv/bin/activate
```

On Windows.

```
venv\Scripts\activate
```

## Installing dependencies

Now that we are in our **virtual enviroment**, we have to install all of our projects dependencies. We can do that by entering this command.

```
pip install -r requirements.txt
```

## Selecting a Day_(number) to run

### Creating the database

After that, cd into the Day_(number) you want to run and enter this command so that it can create the SQLite database for us.

```
python manage.py syncdb
```

### Running the server on localhost:8000

Now we can run the project by entering the following.

```
python manage.py runserver
```

Visit in your **browser** this url and you should see the home page.

```
localhost:8000
```

License
=======
All of "django-workshop" is licensed under the MIT license.

Copyright (c) 2014 Jose E Padilla

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
