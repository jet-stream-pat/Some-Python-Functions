a_number = 5
id(a_number)
type(a_number)

another_number = 6.0
type(another_number)

name = ("patrick")
id(name)
type(name)

# running the id function with the variable in the shell gives me a unique id number for each object
# running the type function with the variable in the shell gives me the type/class of the object, either string (str), integer (int), float (float) or list (list)
# note tha the value of the object is simply obtained by running the code, i.e., running the object 'name' in the shell will give the value 'patrick'


my_list = ['hello']

# Get the ID
id_of_list = id(my_list)

# Get the type
type_of_list = type(my_list)

# Get the value
value_of_list = my_list[0]

print("ID:", id_of_list)
print("Type:", type_of_list)
print("Value:", value_of_list)
