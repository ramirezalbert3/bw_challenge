import re
from flask import Flask, request, jsonify
from password_check import password_check, _rules_dictionary

app = Flask(__name__)

@app.route('/password_check', methods=['GET'])
def wrapped_password_check():
    password = request.get_json()['password']
    result = password_check(password, _rules_dictionary())
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
