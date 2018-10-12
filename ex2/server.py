import re
from flask import Flask, request

app = Flask(__name__)

@app.route('/password_check', methods=['GET'])
def password_check():
    # semi-customizable rules here
    rules_dict =  {'length': 10,
                   'must_have_numbers': True,
                   'must_have_caps': True}

    password = request.get_json()['password']
    str_len = len(password) >= rules_dict['length']
    
    has_numbers = True
    if rules_dict['must_have_numbers']:
        has_numbers = bool(re.search(r'\d', password))
    
    has_caps = True
    if rules_dict['must_have_caps']:
        has_caps = bool(re.search(r'[A-Z]+', password))
    
    return str(str_len and has_numbers and has_caps)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
