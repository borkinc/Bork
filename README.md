# Bork
A simple database application for photo messaging in a social context, like Instagram but based on chat groups.

### Objectives
* Understand the design, implementation and use of an application backed by a database system.
* Understand the use of the E-R model for database application design.
* Gain experience by implementing applications using layers of increasing complexity and fairly complex data structures.
Gain further experience with Web programming concepts including REST and HTTP.
 
## Installation
Must have installed **Python3.6**

Assuming project root
* MacOs/Ubuntu
``` Shell
source venv/bin/activate
```
* Windows
```Shell
.\venv\Scripts\activate
```
```Shell
pip install -r requirements.txt
```
After installing required packages, set the environment variables for SECRET_KEY and JWT_SECRET_KEY. I recommend using 
[secrets](https://docs.python.org/3/library/secrets.html) python module to generate keys
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
To run app with Development/Production settings, set the environment variable.
* Development
  * MacOs/Ubuntu
    ``` Shell
    export FLASK_SETTINGS="DevelopmentConfig"
    ```
   * Windows
    ```Shell
    set FLASK_SETTINGS="DevelopmentConfig"
    ```
* Production
  * MacOs/Ubuntu
    ``` Shell
    export FLASK_SETTINGS="ProductionConfig"
    export DATABASE_URL="DATABASE URL HERE"
    ```
   * Windows
    ```Shell
    set FLASK_SETTINGS="ProductionConfig"
    set DATABASE_URL="DATABASE URL HERE"
    ```


## Authors and acknowledgment
* **Christian Pérez Villanueva** - [Christianperez34](https://github.com/ChristianPerez34)
* **Javier Bustillo Hernandez** - [javierbustillo](https://github.com/javierbustillo)