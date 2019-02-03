import bcrypt as bcrypt
from flask import Flask, request

from Handlers.Users import Users

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=['POST'])
def create_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = Users(username=username, hashed_password=hashed_password)
        return "added user"


if __name__ == '__main__':
    app.run()
