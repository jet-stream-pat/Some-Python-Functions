# breaking down a function

# function starts with the 'def' keyword
# 'greet_student' is the name of the function
def greet_student(student):
# the parameter inside the brackets is 'student'
# parameters are variables listed inside the brackets in the function definition
# parameters are considered placeholders for values that will be passed into the function when it's called

# using triple quotation marks opens a 'docstring'
# docstrings are used to explain what the function does
    """ function is designed to generate a greeting message about a given student """

# for my function I have decided on using a greeting message
# variable 'greeting' is created
# 'Hello ' is a string literal that will be displayed at the beginning of the greet_student message
# + student < concatenates the value of the 'student' parameter to the 'Hello ' string
# e.g. if the student's name is Hugo, then 'greeting' will become 'Hello Hugo' 
    greeting = "Hello " + student

# The return statement specifies what value the function should return when the function is called
# in my case the function will return the 'greeting' variable which contains the complete greeting message
    return greeting

# 'greet_student("Patrick")' below calls/executes the 'greet_student' function with 'Patrick' as the argument for the 'student' parameter
# arguments are the actual values or variables passed to the function when calling it
result = greet_student("Patrick")
# the line above demonstrates that 'greet_student("Patrick")' is assigned to the created variable 'result'
# since 'Patrick' is passed as the argument, the function will return 'Hello Patrick' and the variable 'result' will store this value 

print(result)
# printing the variable 'result' will give the output 'Hello Patrick'
# this is because the 'result' variable now contains the 'greet_student' function

# Summary
# Function Purpose: greet_student is designed to generate a greeting message for a given student.
# Parameter: It takes one parameter student, which should be a string representing the student's name.
# Return Value: It returns a string "Hello " followed by the student name, forming a complete greeting message.
# Usage: By calling greet_student with a specific student name, you can generate personalized greeting messages for different students.
