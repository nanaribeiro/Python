#Draw fractals with turtle
import turtle

def draw_art():        
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle that draws a square
    brad = turtle.Turtle() #get a turtle
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)

    window.exitonclick() 
draw_art()
