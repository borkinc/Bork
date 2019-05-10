![Logo](https://github.com/borkinc/BorkGUI/blob/master/src/img/dog.svg)
# Bork

![Code Quality](https://img.shields.io/badge/pylint-8.93%2F10-brightgreen.svg)

Bork is a simple database application for photo messaging in a social context, like Instagram but based on chat groups. This repository holds the server-side implementation of the app. The data in the application is managed by a relational database system and exposed to client applications through a REST API. Moreover, the implementation conforms to a Model-View-Controller design pattern.
 
## Table of Contents
* [Technologies](#technologies)
* Installation
* License
* Authors and Acknowledgement

## Technologies
* [Python3.6](https://www.python.org/downloads/) - interpreted, high-level, general-purpose programming language
* [Flask](https://github.com/pallets/flask) - micro web framework written in Python
* [Psycopg2](http://initd.org/psycopg/) - PostgreSQL adapter for the Python
* [Gunicorn](https://gunicorn.org/) - Python Web Server Gateway Interface HTTP server
* [Cloudinary](https://github.com/cloudinary/pycloudinary) - cloud-based image and video management solution
* [Pylint](https://www.pylint.org/) - source-code, bug and quality checker for the Python programming language  

## Installation
[Python3.6](https://www.python.org/downloads/) must be installed and in **PATH**

Run the following from a terminal
```Shell
pip install -r requirements.txt
```

Default **SECRET_KEY** and **JWT_SECRET_KEY** are used. Set the environment variables for the keys previously mentioned for personal use. 

* MacOs/Ubuntu
``` Shell
export SECRET_KEY="YOUR_SECRET_KEY_HERE"
export JWT_SECRET_KEY="YOUR_SECRET_KEY_HERE"
```
* Windows
```Shell
set SECRET_KEY="YOUR_SECRET_KEY_HERE"
set JWT_SECRET_KEY="YOUR_SECRET_KEY_HERE"
```
To run app with Development/Production settings, set the environment variables. Production settings require a database url for database connections and a cloudinary account to serve images.
* Development
  * MacOs/Ubuntu
    ``` Shell
    export FLASK_SETTINGS=DevelopmentConfig
    ```
   * Windows
    ```Shell
    set FLASK_SETTINGS=DevelopmentConfig
    ```
* Production
  * MacOs/Ubuntu
    ``` Shell
    export FLASK_SETTINGS=ProductionConfig
    export DATABASE_URL="DATABASE URL HERE"
    export CLOUDINARY_CLOUD_NAME="CLOUD_NAME_HERE"
    export CLOUDINARY_API_KEY="API_KEY_HERE"
    export CLOUDINARY_API_SECRET="API_SECRET_HERE"
    ```
   * Windows
    ```Shell
    set FLASK_SETTINGS=ProductionConfig
    set DATABASE_URL="DATABASE URL HERE"
    set CLOUDINARY_CLOUD_NAME="CLOUD_NAME_HERE"
    set CLOUDINARY_API_KEY="API_KEY_HERE"
    
## License
```
MIT License

Copyright (c) 2019 borkinc

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
```

## Authors and acknowledgment
* **Christian Pérez Villanueva** - [Christianperez34](https://github.com/ChristianPerez34)
* **Javier Bustillo Hernandez** - [javierbustillo](https://github.com/javierbustillo)