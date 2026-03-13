def add_one(number):
    """ adds one to an input number """
    result = number + 1
    return result
result = add_one(5)
print (result)


def stone_to_pounds(number):
    """ converts stone to pounds """
    stone = number * 14
    return stone
stone = stone_to_pounds(12)
print(stone)


def lucky_number(number):
    """ input number between 1 & 9 transformed into 4 digit lucky number """
    digit_1 = number + 1
    digit_2 = number * 9
    digit_3 = number + 70
    digit_4 = number * 1000
    result = digit_1 + digit_2 + digit_3 + digit_4
    return result
result = lucky_number(9)
print(result)


def count_characters(text):
    """ counts the amount of characters within an input string """
    return len(text)
result = count_characters('Welcome to Python')
print(result)


def is_adult(age):
    """ determines whether a person is an adult or not """
    if age >= 18:
        return True
    else:
        return False

person_age = 10

if is_adult(person_age):
    print ('Adult')
else:
    print ('Not an Adult')


def fee_waiver(savings):
    """ determines if a customer is eligible for a Fee Waiver """
    if savings <= 2000:
        return True
    else:
        return False

account_total = 2000

if fee_waiver(account_total):
    print ('eligible for Fee Waiver')
else:
    print ('not eligible for Fee Waiver')


        
