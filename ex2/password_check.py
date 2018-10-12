import sys
import re

def password_check(password, rules_dict):
    '''
    Verify that any given password string complies
    with the requirements defined in the dictionary
    '''
    str_len = len(password) >= rules_dict['length']
    
    has_numbers = True
    if rules_dict['must_have_numbers']:
        has_numbers = bool(re.search(r'\d', password))
    
    has_caps = True
    if rules_dict['must_have_caps']:
        has_caps = bool(re.search(r'[A-Z]+', password))
    
    return str_len and has_numbers and has_caps

def _rules_dictionary(length=10, must_have_numbers=True, must_have_caps=True):
    return {'length': length,
            'must_have_numbers': must_have_numbers,
            'must_have_caps': must_have_caps}

if __name__ == "__main__":
    '''
    Other arguments than the 1st one ignored
    no input checking whatsoever
    '''
    try:
        password = sys.argv[1]
        print(password_check(password, _rules_dictionary()))
    except IndexError as e:
        raise Exception('Provide password as argument!') from e
