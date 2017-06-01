import turtle #draws things on computer

def draw_square(square_turtle):
    counter = 0
    while counter < 4:
        square_turtle.forward(100)
        square_turtle.right(90)
        counter = counter + 1
        
def draw_circle(circle_turtle):    
    circle_turtle.circle(100)

def draw_triangle(triangle_turtle):
    triangle_turtle.right(80)
    triangle_turtle.backward(80)
    triangle_turtle.right(80)
    triangle_turtle.forward(80)
    triangle_turtle.left(130)
    triangle_turtle.forward(100)
    
def draw_art():        
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle that draws a square
    brad = turtle.Turtle() #get a turtle
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for aux in range(0, 72):
        draw_square(brad)
        brad.right(5)
        aux = aux + 1
    #Create the turtle that draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    #draw_circle(angie)
    #Creates the turtle that draws a triangle
    troy = turtle.Turtle()
    troy.shape("circle")
    troy.color("white")
    #draw_triangle(troy)
    
    window.exitonclick() 
draw_art()
