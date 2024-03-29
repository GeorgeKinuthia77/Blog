# Blog

## Description
This is a web application that allows users to express themselves using a blog posts. They they first create an account then log in to start creating blogs..
## Author
George Njoroge(11/8/2019)

## links
Github link:https://github.com/GeorgeKinuthia77/Blog

Live link:https://gnjoro-blog.herokuapp.com/

## The user can:

* See various blog posts

* View blogposts they like

* See the latests posts

* Subscribe to latest post service

## Setup/Installation Requirements

* Prerequisites

* python3.6

* pip

* Virtual environment(virtual)

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

## Testing the Application
To run the tests for the class files:

    $ python3.6 manage.py test

## Technologies Used

* Python 3.6

* Flask

* bootstrap

## BDD

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| Display latest blogs | On page load | List of various blogs I have written |
| Registration | Submit regitration form | User creates an account and receives welcome email |
| Subscription | Submit subscription form| User receives email eb=very time there is a new post|
| Edit posts(writer) | Submit edit post | The post is updated with new data from user |
| Delete posts(writer) | Click delete post | Post is deleted |
| Delete comments(writer) | Click delete comment | Comment is deleted |


## Support and contact details
For any questions, troubleshooting or contributions,  find me on:
* Email: gnjoro077@gmail.com

* Contact: 0704282877

### License

[MIT LICENSE}
This project is licensed under the MIT License.

Copyright (c) 2019 George Kinuthia

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
