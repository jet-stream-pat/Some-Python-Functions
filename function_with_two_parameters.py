def add_binary(number_1, number_2):
    if number_1 == 0 and number_2 == 0:
        return 0
    elif number_1 == 0 and number_2 == 1:
        return 0
    elif number_1 == 1 and number_2 == 0:
        return 0
    else:
        return 1

result = add_binary(1,1)

print (result)
