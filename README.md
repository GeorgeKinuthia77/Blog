# Blog

## Description
This is a web application that allows users to express themselves using a blog posts. They they first create an account then log in to start creating blogs..
## Author
George Njoroge(11/8/2019)

## The user can:

See various blog posts

View blogposts they like

See the latests posts

Subscribe to latest post service

## Setup/Installation Requirements
Prerequisites

python3.6

pip

Virtual environment(virtual)

## Cloning and running
Clone the application using git clone(this copies the app onto your device). In terminal:

    $ git clone https://github.com/GeorgeKinuthia77/Blog
    $ cd Blogging
Creating the virtual environment

    $ python3.6 -m venv --without-pip virtual
    $ source virtual/bin/env
    $ curl https://bootstrap.pypa.io/get-pip.py | python
Installing Flask and other Modules

    $ python3.6 -m pip install Flask
    $ python3.6 -m pip install Flask-Bootstrap
    $ python3.6 -m pip install Flask-Script
    $ python3.6 -m pip install -r requirements.txt
Run the application:

    $ chmod a+x start.sh
    $ ./start.sh
