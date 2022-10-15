from sys import prefix
import unittest
from credit_card_validator import credit_card_validator

"""
Visa
        Prefix(es): 4
        Length: 16
MasterCard
        Prefix(es): 51 through 55 and 2221 through 2720 
        Length: 16
American Express
        Prefix(es): 34 and 37
        Length: 15

"""
message = "Fail"
class Testcase(unittest.TestCase):

# ====================================================================Visa Testing============================================================================== #
        # Verifies a valid Visa card with valid length and prefix
        # Generated through random card generator website
        # https://bestccgen.com/visa-card-generator.php
        def test_valid_visa1(self):
                a = 4079585476130230
                self.assertFalse(credit_card_validator(a), message)

        # Verifies a valid Visa card with valid length and prefix
        # Generated through random card generator website
        # https://bestccgen.com/visa-card-generator.php
        def test_valid_visa2(self):
                a = 4535893361574654
                self.assertFalse(credit_card_validator(a), message)
        
        # Tests an invalid Visa that does not have correct length
        # Manually created by placing number length less than 16 or 15
        def test_invalid_visa1(self):
                a = 41620700136113
                self.assertFalse(credit_card_validator(a), message)
                
        # Tests an invalid Visa that does not have correct prefix
        # Manually created by placing random number with incorrect prefix
        def test_invalid_visa2(self):
                a = 1162070013611388
                self.assertFalse(credit_card_validator(a), message)
                
        # Tests an invalid Visa that does not have correct length or prefix
        # Manually created by placing number length less than 16 or 15 and having an incorrect prefix
        def test_invalid_visa3(self):
                a = 11620700136113
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies a Visa card with an invalid length of 15 and prefix
        # Generated through random card generator website
        # https://bestccgen.com/visa-card-generator.php
        def test_invalid_visa4(self):
                a = 450625221205065
                self.assertFalse(credit_card_validator(a), message)
                
        
# ====================================================================American Express Testing============================================================================== #
        # Verifies a valid American Express card with valid length and prefix
        # Generated through random card generator website
        # https://bestccgen.com/amex-card-generator.php
        def test_valid_americanexp1(self):
                a = 349773310236130
                self.assertFalse(credit_card_validator(a), message)

        # Verifies a valid American Express card with valid length and prefix of max 37
        # Created manually by placing correct length and prefix
        def test_valid_americanexp2(self):
                a = 379869244557805
                self.assertFalse(credit_card_validator(a), message)
                
        # Verifies a valid American Express card with valid length and prefix within middle of range of accepted values 35
        # Created manually by placing correct length and prefix
        def test_valid_americanexp3(self):
                a = 359869244557805
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies an invalid American Express card with invalid length of 14
        # Created manually by placing incorrect length and valid prefix
        def test_invalid_americanexp1(self):
                a = 35986924455780
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies an invalid American Express card with valid length but prefix outside of min range of 34: 33
        # Created manually by placing correct length and invalid prefix
        def test_invalid_americanexp2(self):
                a = 33986924455780
                self.assertFalse(credit_card_validator(a), message)

        # Verifies an invalid American Express card with valid length but prefix outside of max range of 37: 38
        # Created manually by placing correct length and invalid prefix
        def test_invalid_americanexp3(self):
                a = 38986924455780
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies an invalid American Express card with invalid length of 16 and valid prefix within range 34 - 37
        # Created manually by placing correct length and invalid prefix
        def test_invalid_americanexp4(self):
                a = 35620700136113
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies a American Express card with invalid length of 16 and valid prefix
        # Generated through random card generator website and removing a number
        # https://bestccgen.com/amex-card-generator.php
        def test_invalid_americanexp5(self):
                a = 3574727844710641
                self.assertFalse(credit_card_validator(a), message)

# ====================================================================Mastercard Testing============================================================================== #
     
        # Verifies a Master Card type 1 with valid length and prefix
        # Generated using a random card generator
        # https://bestccgen.com/master-card-generator.php
        def test_valid_mastercard1(self):
                a = 5372074903653800
                self.assertFalse(credit_card_validator(a), message)

        # Verifies a Master Card type 2 with valid length and prefix
        # Generated using a random card generator
        # https://bestccgen.com/master-card-generator.php
        def test_valid_mastercard2(self):
                a = 2600074903653800
                self.assertFalse(credit_card_validator(a), message)
                
        
        # Verifies a Master Card type 1 with valid length and an invalid prefix outside of range: 50
        # Number created manually by placing prefix into an old generated number
        def test_invalid_mastercard1(self):
                a = 5000074903653800
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies a Master Card type 1 with valid length and an invalid prefix outside of range: 56
        # Number created manually by placing prefix into an old generated number
        def test_invalid_mastercard2(self):
                a = 5600074903653800
                self.assertFalse(credit_card_validator(a), message)

        # Verifies a Master Card type 2 with valid length and an invalid prefix outside of range: 2220
        # Number created manually by placing prefix into an old generated number
        def test_invalid_mastercard3(self):
                a = 2220074903653800
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies a Master Card type 2 with valid length and an invalid prefix outside of range: 2721
        # Number created manually by placing prefix into an old generated number
        def test_invalid_mastercard4(self):
                a = 2721074903653800
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies a Master Card type 2 with invalid length of 14 and valid prefix
        # Number generated using a random card generator
        # https://bestccgen.com/master-card-generator.php
        def test_invalid_mastercard5(self):
                a = 53720733730384
                self.assertFalse(credit_card_validator(a), message)
        
        # Verifies a Master Card type 2 with invalid length of 14 and valid prefix
        # Number created manually by using an old number from a random card generator and changing the prefix
        # https://bestccgen.com/master-card-generator.php
        def test_invalid_mastercard6(self):
                a = 26000749036538
                self.assertFalse(credit_card_validator(a), message)

        # Verifies a Master Card type 1 with invalid length of 15 and valid prefix
        # Generated using a random card generator and removing a number
        # https://bestccgen.com/master-card-generator.php
        def test_invalid_mastercard7(self):
                a = 260007490365380
                self.assertFalse(credit_card_validator(a), message)
        
        
        
                
        


