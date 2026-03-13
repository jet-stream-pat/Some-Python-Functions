# lines 1 -5 consist of the definition
def list_length(a_list):
    length = 0
    for item in a_list:
        length = length + 1
    return length
	
test_list = ['a', 'b']
# line 7 sees the list ['a', 'b'] assigned to 'test_list'
length_test_list = list_length(test_list)
# line 8 sees value of list_length(test_list) is assigned to the length_test_list. To compute the value of 'list_length'(test_list), the function list_length() is called with the argument 'test_list' 
print('The list', test_list, 'contains',
    length_test_list, 'items.')

