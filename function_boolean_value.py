# example of a function that returns a boolean code
# note that function names are usually verbs, like 'get_sum', 'compute_total',etc
# however, special cases where functionss that return a boolean value often begin with 'is', 'has', or 'can'
def is_freezing(temperature):
    return temperature < 0
freezing = is_freezing(-3)
print(freezing)
# code above returns true into the console because is_freezing is less than 0
# this is due the value 'temperature < 0' being returned,
# and in the next line, calling the function 'is_freezing' assigning the value -3 to it, and storing it to the created variable 'freezing'
# finally printing the created variable 'freezing' 
