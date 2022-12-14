
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

visa = 4
mastercard = range(51, 56)
mastercard2 = range(2221, 2721)
americanexp = range(34, 38)


def credit_card_validator(num):
    card_type = credit_card_length(num)
# If the length of the credit card passes, check through others
    if card_type == 1:
        if (valid_prefix_amrcnexp(num)):
            return False
    elif card_type == 2:
        if valid_prefix(num, getSize(visa)):
            return False
        elif (valid_prefix(num, 4)):
            return False
        elif (valid_prefix(num, 2)):
            return False
    return True

# Assess whether the values entered are of valid digit sizes
# Returns true if passes


def credit_card_length(num):
    if (getSize(num) == 15):
        return 1
    elif (getSize(num) == 16):
        return 2
    else:
        return 0

# Following code block below is from GeeksforGeeks
# Finds the length of an integer by converting the integer into a string
# https://www.geeksforgeeks.org/program-credit-card-number-validation/


def getSize(d):
    # Converts integer into a string and finds the length of that string
    num = str(d) + ""
    return len(num)

# Following code block is from GeeksforGeeks
# This function checks if number's prefix is valid


def valid_prefix(num, k):
    # Passes the card number and length of prefix
    # If the number has a prefix of '4' then a Visa card has been found
    if get_Prefix(num, getSize(k)) == 4:
        print("Visa found!")
        return True
    # If American Express card was not found, check if it is a mastercard
    elif (mastercard_check(get_Prefix(num, 2))):
        print("Mastercard type 1 found!")
        return True
    # If Master Card type 1 not found, check if it is a type 2
    elif (mastercard_check2(get_Prefix(num, 4))):
        print("Mastercard type 2 found!")
        return True
    # If the number is not a valid credit card, return false
    else:
        return False


def valid_prefix_amrcnexp(num):
    # If prefix of 4 was not found, check if card fits American Express prefix
    if (americanexp_check(get_Prefix(num, 2))):
        print("American Express card found!")
        return True
    return False

# Functions accepts a value (k) and checks if that value
# is within the prefix range of American Express Card type (34 - 37)
# Returns True if value is within range


def americanexp_check(k):
    for i in americanexp:
        print(i)
        if i == k:
            print("Value found: " + str(i))
            return True
        else:
            print("Value was not found!")
    return False

# Functions accepts a value (k) and checks if that value
# is within the prefix range of Master Card type 1 (51 - 55)
# Returns True if value is within range


def mastercard_check(k):
    for i in mastercard:
        if i == k:
            print("Found value within mastercard: " + str(i))
            return True
    return False

# Functions accepts a value (k) and checks if that value
# is within the prefix range of Master Card type 2 (2221 - 2270)
# Returns True if value is within range


def mastercard_check2(k):
    for i in mastercard2:
        if i == k:
            print("Found value within mastercard: " + str(i))
            return True
    return False

# Code modeled after GeeksforGeeks function
# Returns the first K number of digits from number
# If the number of digits (k) in number is less than k, return the number.
# https://www.geeksforgeeks.org/program-credit-card-number-validation/


def get_Prefix(num,  k):
    if (getSize(num) > k):
        number = str(num) + ""
        print("Returning prefix: " + str(int(number[0:k])))
        return int(number[0:k])
    return num
