#def list_length(a_list):
    #length = 0
    #for item in a_list:
        #length = length + 1
    #return length
	
#test_list = ['a', 'b']
#length_test_list = list_length(test_list)
#print('The list', test_list, 'contains',
    #length_test_list, 'items.')

# the code below explores how the interpreter steps through the program above /\
# each print statement below indicates which line in the program above has been executed
# e.g., 'print 1' tells me that line 1 has been executed
# print 0 tells me that execution of the program has started

print(0)

def list_length(a_list):
  print(1)
  length = 0
  print(2)
  for item in a_list:
    print(3)
    length = length + 1
    print(4)
  return length

print(6)
test_list = ['a', 'b']

print(7)
length_test_list = list_length(test_list)
print(8)
print('The list', test_list, 'contains', length_test_list, 'items.')
print(10)
