# Bork
A simple database application for photo messaging in a social context, like Instagram but based on chat groups.

### Objectives
* Understand the design, implementation and use of an application backed by a database system.
* Understand the use of the E-R model for database application design.
* Gain experience by implementing applications using layers of increasing complexity and fairly complex data structures.
Gain further experience with Web programming concepts including REST and HTTP.

### Phase I
In this phase there is **no interaction** with the database server! Interactions with the server will be made with Postman.
 - [x] E-R model, illustrating the data to be stored in the site.
 - [ ] Register a user
 - [ ] Login with a user
 - [ ] Create dummy chat group
 - [ ] Add user to contacts list based on name, last name, and either phone or email
 - [ ] Add a contact to a chat group
 - [ ] Remove a user from the contacts list
 - [ ] Remove a user from the contacts list
 - [ ] Remove a chat group (only the owner of said chat may execute this operation)
 - [ ] Post photo and message to a chat group. The message may include hashtags
 - [ ] See the photo, the original message that came with the photo, and any replies
 - [ ] Like/Dislike a photo
 - [ ] Reply to messages
 
 #### Optional
 - [ ] Post a video to a group
 - [ ] Run application from the cloud (Heroku, AWS, etc)
 - [ ] Run on a mobile phone
 
 
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


## Authors and acknowledgment
* **Christian Pérez Villanueva** - [Christianperez34](https://github.com/ChristianPerez34)
* **Javier Bustillo Hernandez** - [javierbustillo](https://github.com/javierbustillo)