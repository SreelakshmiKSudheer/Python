import turtle
tur = turtle.Turtle()           # giving a name

#  square
for i in range(4):
    tur.forward(50)
    tur.right(90)

# star
for i in range(5):
    tur.forward(50)
    tur.right(144)
    
turtle.done()                   

'''
In Python, the function turtle.done() is used to start the event loop in the turtle graphics module (turtle). 
It calls Tkinter's main loop function and does not require any arguments. 
This function is used to keep the turtle graphics window open until the user closes it or terminates the program. 
It is commonly used at the end of the turtle graphics code to prevent the window from closing immediately.
'''