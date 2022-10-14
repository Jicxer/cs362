from sys import prefix
import unittest
from credit_card_validator import credit_card_validator

def test11(self):
        message = "Test value is not false"
        self.assertFalse(credit_card_validator("45"), message)
        
message = "Fail"
class Testcase(unittest.TestCase):
        
        def test1(self):
                a = 1369079890
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies a Master Card with valid lengths and prefix
        # Picked using a number generator
        def test2(self):
                a = 5574841807576444
                self.assertFalse(credit_card_validator(a), message)