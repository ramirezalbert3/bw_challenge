import password_check as pc
import unittest

# These 3 should return False with the given defaults
short_passw = ['aBcd1', '2abcD', 'Ab3cD',
               'AbCd1wXyZ']

nocaps_passw =  ['abcdewxyz1', '2abcdvwxyz', 'ab3cdevwyz',
                 'abcd12evwxyz', '2abcdvwxyzabcdewxyz1']

nonums_passw =  ['abcdewxyzFG', 'QWabcdvwxyz', 'abQWERcdevwyz',
                 'abcdEVwxyz', 'AabcdvwxyzabcdewxyzZ']

# This should return True with the given defaults
strong_passw =  ['1Abcdevwxyz', 'abcdewxy9FG', 'QWabcdv34yz', 'abQWERcde57yz',
                 'abcdEVwxy0', 'Aabcdvwxyz101abyzZ']

class TestDefaults(unittest.TestCase):
    def test_short(self):
        rules = pc._rules_dictionary()
        for pw in short_passw:
            with self.subTest(i=pw):
                self.assertFalse(pc.password_check(pw, rules))

    def test_nocaps(self):
        rules = pc._rules_dictionary()
        for pw in nocaps_passw:
            with self.subTest(i=pw):
                self.assertFalse(pc.password_check(pw, rules))

    def test_nonums(self):
        rules = pc._rules_dictionary()
        for pw in nonums_passw:
            with self.subTest(i=pw):
                self.assertFalse(pc.password_check(pw, rules))

    def test_strong(self):
        rules = pc._rules_dictionary()
        for pw in strong_passw:
            with self.subTest(i=pw):
                self.assertTrue(pc.password_check(pw, rules))

# Non-Default test cases
class TestShortPasswordsAllowed(unittest.TestCase):
    ''' This proves that short passwords are returned True if allowed'''
    def test_supershort(self):
        rules = pc._rules_dictionary(length=4)
        self.assertFalse(pc.password_check('ab1', rules))

    def test_short(self):
        rules = pc._rules_dictionary(length=4)
        for pw in short_passw:
            with self.subTest(i=pw):
                self.assertTrue(pc.password_check(pw, rules))

    def test_strong(self):
        rules = pc._rules_dictionary(length=4)
        for pw in strong_passw:
            with self.subTest(i=pw):
                self.assertTrue(pc.password_check(pw, rules))

class TestLongPasswordsAllowed(unittest.TestCase):
    '''
    This proves that "long" passwords are returned False
    if length requirements are high
    '''
    def test_superlong(self):
        rules = pc._rules_dictionary(length=20)
        self.assertTrue(pc.password_check('Aabcdvwxyz101abcdewxyzZ', rules))

    def test_short(self):
        rules = pc._rules_dictionary(length=20)
        for pw in short_passw:
            with self.subTest(i=pw):
                self.assertFalse(pc.password_check(pw, rules))

    def test_strong(self):
        rules = pc._rules_dictionary(length=20)
        for pw in strong_passw:
            with self.subTest(i=pw):
                self.assertFalse(pc.password_check(pw, rules))

class TestNoNumsRequired(unittest.TestCase):
    ''' This proves that passwords without numbers are returned True if allowed'''
    def test_nonums(self):
        rules = pc._rules_dictionary(length=10,
                                     must_have_numbers=False,
                                     must_have_caps=True)
        for pw in nonums_passw:
            with self.subTest(i=pw):
                self.assertTrue(pc.password_check(pw, rules))

    def test_strong(self):
        rules = pc._rules_dictionary(length=10,
                                     must_have_numbers=False,
                                     must_have_caps=True)
        for pw in strong_passw:
            with self.subTest(i=pw):
                self.assertTrue(pc.password_check(pw, rules))

class TestNoCapsRequired(unittest.TestCase):
    ''' This proves that passwords without caps are returned True if allowed'''
    def test_nocaps(self):
        rules = pc._rules_dictionary(length=10,
                                     must_have_numbers=True,
                                     must_have_caps=False)
        for pw in nocaps_passw:
            with self.subTest(i=pw):
                self.assertTrue(pc.password_check(pw, rules))

    def test_strong(self):
        rules = pc._rules_dictionary(length=10,
                                     must_have_numbers=True,
                                     must_have_caps=False)
        for pw in strong_passw:
            with self.subTest(i=pw):
                self.assertTrue(pc.password_check(pw, rules))

if __name__ == '__main__':
    unittest.main()
