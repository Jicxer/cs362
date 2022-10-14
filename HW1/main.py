import unittest
from credit_card_validator import credit_card_validator
# Verifies if Master Cards with valid lengths and invalid check bits returns False
# Picked using Category Partition Testing
def test11(self):
        self.assertFalse(credit_card_validator("...."))

if __name__ == '__main__':
    unittest.main()
    

# Visa 