# mimo function practice
# functions are handy for reusing code
# functions are used to group related code and perform the task in one place
# start with 'def' to define a function
# next is create a function name like 'greet_user' followed by brackets () and a colon :
def greet_user(): # note that the colon signifies the beginning of the functions code block
    print("Good morning, Patrick") # note the double indentation with the code blocks
    print("Welcome back.")
greet_user() # to run the code, I need to call the function
# to call the function, I dedent back to the start of the line and type the function name, followed by brackets - greet_user()

# variable inside function
def greet_patrick(): 
    name = "Patrick." # variables inside functions can be used inside functions
    print("Hello,", name)
greet_patrick()

# PASSING VALUES
# passing a value to a function without repeating code
# to pass the value to a function, we first add a variable called a 'parameter' inside brackets of the function.
def greet(name): # here the parameter is 'name', and the parameter acts like a variable that stores a value, but it doesn't have a value at this moment
    print(f"Hello, {name}") # revise the 'f' code
greet("Laura") # to pass the value to a variable, it's places the value between the brackets when the function is called
greet("Patrick") # like here where the value 'Patrick' is placed within brackets and then function 'greet' is called
# prints 'Hello, Laura' and on the line below also prints 'Hello, Patrick' into the console
# another example \/
def user_status(status): # parameter is 'status', and the parameter acts like a variable that stores a value, but it doesn't have a value at this moment
    print(f"Patrick: {status}") 
user_status("Active") # here the value 'Active' is passed to a variable when the function 'user_status' is called.
# prints 'Patrick: Active' into the console once the function is called.

# RETURN
# a function can return a value to the code that called it
# if the outcome of a function task is needed, use the 'return' keyword to achieve this
# to return a value from a function, add 'return' as a keyword followed by the value to return
def give_me_ten():
    return 10 # 'return' keyword
print(give_me_ten()) # to use the return value of a function, simply call the function and use it like any other value
# another 'return' example below
def add_greeting(user):
    greeting = "Greetings " + user
    return greeting
result = add_greeting("Patrick") # we can store the return value in a variable by calling the function and then storing it to a variable
print(result)




