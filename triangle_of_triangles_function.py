# STEP1
# defining a function to replace duplicate code
from turtle import *
# this function has NO parameters, so the space in between the brackets in blank
def draw_triangle():
    """ Defining the 'draw_triangle function to replace duplicate code
the triangle will be an equilateral triangle with sides of 40 length""" # remember to use a docstring to document what the function does
    for sides in range(1,4): # this is the duplicate code for the 'draw_3_triangles' program saved in python/tm112_programs/turtle folder
        forward(40)
        left(120)
# note by running this code and entering the fuction name 'draw_triangle()' in the shell, turtle will ONE triangle

# STEP2
# combine the function with the original 'draw_3_triangles_for_loop' program
draw_triangle() # calling the function to initiate the first triangle drawing
# move to next triangle start position
penup()
left(90)
forward(100)
right(90)
pendown()

draw_triangle()# calling the function to initiate the second triangle drawing
# move to next triangle start position
penup()
right(90)
forward(100)
left(90)
forward(100)
pendown()

# move to next triangle start position
draw_triangle()# calling the function to initiate the third triangle drawing

# the program above successfully uses a function to replace the initial duplicate code in the 'draw_3_triangles_for_loop'

done() # 'done()'is a method used to signal the Turtle graphics window to wait for the user to close the window manually
