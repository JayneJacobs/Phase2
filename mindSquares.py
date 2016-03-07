import turtle


def draw_square(some_turtle):
   for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        #some_turtle.speed(10)
        
    #
    #exit = window.exitonclick()
    #return exit
    
def draw_circle(other_turtle):
    for j in range(1,5):
        other_turtle.circle(100)
        other_turtle.right(10)
        #.speed(10)
def draw_sketch():
    
    window = turtle.Screen()
    window.bgcolor("red")
    #brad.right(5)
    brad = turtle.Turtle()
    brad.speed(40)
    brad.color("yellow")
    brad.shape("triangle")
    

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("white")
    angie.speed(50)
    for k in range(1,75):
        draw_square(brad)
        brad.right(5)
        draw_circle(angie)
    window.exitonclick()

draw_sketch()
