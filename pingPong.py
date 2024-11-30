import turtle

wind = turtle.Screen() #intialize screen
wind.title ("ping Pong By rayane chahititlne") #set the e of the window
wind.bgcolor("black") #set the background color of the window
wind.setup(width=800, height=600) #set the width and height of the window
wind.tracer (0) #stops the window from updating automatically

#madrab1
madrab1 = turtle.Turtle ()
madrab1.speed (0)
madrab1.shape("square")
madrab1.color("blue") 
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(350, 0)
#madrab2
madrab2 = turtle.Turtle ()
madrab2.speed (0)
madrab2.shape("square")
madrab2.color("blue") 
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(-350, 0)
#ball
ball = turtle.Turtle ()
ball.speed ()
ball.shape("square")
ball.color("blue") 
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

def madrab1_up ():
    madrab1.sety(madrab1.ycor()+20)
def madrab1_down ():
    madrab1.sety(madrab1.ycor()-20)
def madrab2_up ():
    madrab2.sety(madrab2.ycor()+20)
def madrab2_down ():
    madrab2.sety(madrab2.ycor()-20)

wind.listen()
wind.onkeypress (madrab2_up, "w")
wind.onkeypress (madrab2_down, "s")
wind.onkeypress (madrab1_up, "Up")
wind.onkeypress (madrab1_down, "Down")

while True:
    wind.update()
    ball.setx (ball.xcor()+ball.dx)
    ball.sety (ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor()>390:
        ball.goto(0, 0)
    if (ball.xcor()>390 and ball.ycor()>)
