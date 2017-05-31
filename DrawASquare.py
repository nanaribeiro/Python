import turtle #draws things on computer

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle() #get a turtle
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    
    counter = 0
    while counter < 4:
        brad.forward(100)
        brad.right(90)
        counter = counter + 1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

    troy = turtle.Turtle()
    troy.shape("circle")
    troy.color("white")
    troy.backward(100)
    troy.left(10)

    window.exitonclick() 
draw_shapes()
