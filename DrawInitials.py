#Draw my initials with turtle AR
import turtle
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
    #Creates the turtle that draws a triangle
    troy = turtle.Turtle()
    troy.shape("circle")
    troy.color("white")
    draw_triangle(troy)
    
    window.exitonclick() 
draw_art()
