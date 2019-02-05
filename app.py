from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

users = {}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(user={user_id: users[user_id]})


@app.route('/api/user/<int:user_id>', methods=['POST'])
def add_user(user_id):
    try:
        users.update({user_id: request.form['username']})
    except Exception as e:
        print(e)
    return jsonify(user=users), 200


if __name__ == '__main__':
    app.run(debug=True)
