#'def' used to define a function
#'list_length' in example below is the function name alongside brackets and colon
#'a_list' inside the brackets is the function argument/ function parameter
def list_length(a_list):
    """ Return the length of a list""" # this is a docstring
    length = 0
    for item in a_list:
        length = length + 1
    return length # 'return' is used here to return a value, and here will return the value of 'length'
