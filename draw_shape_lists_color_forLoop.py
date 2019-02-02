import turtle  # import module so you can work with it

# Define window size as constants
window = turtle.Screen()  # create a window (canvas) for the turtle to draw on
window.title("Turtle Demo")  # the title to show at the top of the window
WINDOW_WIDTH = 800  # size constants for easy changing
WINDOW_HEIGHT = 500
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  # set window size (width, height)
window.setworldcoordinates(-70, -70, WINDOW_WIDTH, WINDOW_HEIGHT)  # coord system
# Create the Turtle! Initialize a turtle variable and call the turtle function. 
fred = turtle.Turtle()
fred.speed("fastest")  
fred.shape("turtle")

## 1
## I want a turtle that draws some shapes
## How about an octagon?

for side in range(8): 
    fred.forward(50)
    fred.left(...some number...)    

## 2
## Now I want my turtle to draw 3 octagons! With color!
## Q: 2nd loop? Color goes where? 


## 3
## Now wrap it in a function


## 4
## Add Color Function make them stop signs!
## No, make them 3 different colors...


## 5 
## Now add a fourth octagon! What the heck?








# ## Fully Baked
# def choose_color(index): 
#     colors_list = ["red", "green", "blue"] 
#     return colors_list[index%3]

# #print(choose_color(0))

# ##for loop and range example
# def draw_shape (turtle): 
#     turtle.penup()
#     turtle.goto(50,50)
#     turtle.pendown()
#     for i in range(5):
#         turtle.begin_fill()
#         turtle.color(choose_color(i))
#         num_sides = 5
#         for sid_num in range(num_sides): 
#             turtle.forward(100)
#             turtle.left(360/num_sides)     
#         turtle.end_fill()
#         turtle.penup()
#         turtle.forward(250)
#         turtle.pendown()

# draw_shape(turtle)



# Make turtle graphics appear and run; wait for the user to close the screen
# This MUST be the last statement executed in the script
window.mainloop()
