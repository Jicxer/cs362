
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

#Bugs that can be found:
# 16 digit American Express
# 15 digit visa or master

def credit_card_validator(num):
    pass


visa = 4
mastercard = range(51,56)
mastercard2 = range(2221,2721)
americanexp = range(34,38)

def credit_card_validator(num):
    if credit_card_length(num) == True:                                     #If the length of the credit card passes, check through others
        if (valid_prefix(num,getSize(visa))):
            return False
        elif(valid_prefix(num,2)):
            return False
        elif(valid_prefix(num,4)):
            return False
    return True

# Assess whether the values entered are of valid digit sizes
# Returns true if passes
def credit_card_length(num):
    if (getSize(num) == 16 or getSize(num) == 15):
        return True
    else:
        return False

# Following code block below is from GeeksforGeeks
# This function finds the length of an integer by converting the integer into a string and utilizing len()
# https://www.geeksforgeeks.org/program-credit-card-number-validation/
def getSize(d):
    num = str(d) + ""
    return len(num)

# Following code block is from GeeksforGeeks
# This function checks if number's prefix is valid
def valid_prefix(num, k):                                                        #Passes the card number and length of prefix
    print("Printing K:")
    print(k)
    if get_Prefix(num,getSize(k)) == 4:                                          #If the number has a prefix of '4' then a Visa card has been found
        print("Visa found!")
        return True
    elif(americanexp_check(get_Prefix(num,2)) == True):
        print("American Express card found!")
        return True
    elif (mastercard_check(get_Prefix(num,2)) == True):
        print("Mastercard type 1 found!")
        return True
    elif (mastercard_check2(get_Prefix(num,4)) == True):
        print("Mastercard type 2 found!")
        return True
    else:
        return False

def americanexp_check(k):
    print("Printing k within americanexp_check: " + str(k))
    for i in americanexp:
        if i == k:
            print("Found value within american express: " + str(i))
            return True
    print("Value was: " + str(k))
    return False
            

def mastercard_check(k):
    print("Printing k within mastercard_check: " + str(k))
    for i in mastercard:
        if i == k:
            print("Found value within mastercard: " + str(i))
            return True
    return False

def mastercard_check2(k):
    print("Printing k within mastercard_check: " + str(k))
    for i in mastercard2:
        if i == k:
            print("Found value within mastercard: " + str(i))
            return True
    return False
    
def get_Prefix(num,  k):
    print(k)
    print("printing size of k")
    print(getSize(k))
    if (getSize(num) > k):
        number = str(num) + ""
        print("Returning prefix: " + str(int(number[0:k])))
        return int(number[0:k])
    return num