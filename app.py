from flask import Flask, request, jsonify
from models.users import User

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    # username = request.form.get("username")
    # email = request.form.get("email")
    # password = request.form.get("password")
    # register_date = request.form.get("register_date")
    user = User()  # username, email, password, register_date)
    return jsonify(user.get_all_users())


app.run(debug=True)
