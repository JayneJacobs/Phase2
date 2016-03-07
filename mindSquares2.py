import turtle


def draw_square(some_turtle):
   for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        #some_turtle.speed(10)    

def draw_sketch():
    
    window = turtle.Screen()
    window.bgcolor("red")
    #brad.right(5)
    brad = turtle.Turtle()
    brad.shape("triangle")
    brad.color("yellow")
    brad.speed(40)

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("white")
    angie.speed(50)
    for k in range(1,75):
        draw_square(brad)
        brad.right(5)
        #draw_circle(angie)
    window.exitonclick()

draw_sketch()
