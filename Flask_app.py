from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}  # In-memory user storage

@app.route('/')
def home():
    return "Welcome to the User Management API!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# POST - Add user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = {"name": data.get("name"), "email": data.get("email")}
    return jsonify({"message": "User added!", "user": users[user_id]}), 201

# PUT - Update user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.get_json()
        users[user_id].update({
            "name": data.get("name", users[user_id]["name"]),
            "email": data.get("email", users[user_id]["email"])
        })
        return jsonify({"message": "User updated!", "user": users[user_id]})
    return jsonify({"message": "User not found"}), 404

# DELETE - Remove user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        deleted = users.pop(user_id)
        return jsonify({"message": "User deleted!", "user": deleted})
    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
