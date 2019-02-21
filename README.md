# Bork
A simple database application for photo messaging in a social context, like Instagram but based on chat groups.

### Objectives
* Understand the design, implementation and use of an application backed by a database system.
* Understand the use of the E-R model for database application design.
* Gain experience by implementing applications using layers of increasing complexity and fairly complex data structures.
Gain further experience with Web programming concepts including REST and HTTP.

### Phase I
In this phase there is **no interaction** with the database server!
 - [ ] E-R model, illustrating the data to be stored in the site.
 - [ ] Folder with the working code for the project / Working site. (Contacts API, however, responses should be 
 hard-wired JSON objects)
 
 
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
After installing required packages, set the environment variables for SECRET_KEY and JWT_SECRET_KEY
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


## Authors and acknowledgment