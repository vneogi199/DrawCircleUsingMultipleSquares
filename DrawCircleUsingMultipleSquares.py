import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():
    turtleDrawer = turtle.Turtle()
    turtleDrawer.speed(5)
    turtleDrawer.color("yellow")
    turtleDrawer.shape("classic")
    for i in range(0,36):
        for i in range(0,4):
            turtleDrawer.forward(100)
            turtleDrawer.right(90)
        turtleDrawer.right(10)

    
    window.exitonclick()

draw_square()
