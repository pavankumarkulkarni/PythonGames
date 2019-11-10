# simple ping pong game in python 3
import turtle
import winsound

wn = turtle.Screen()
wn.title("Ping Pong game")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)
pavan_score = 0
vaagmey_score = 0

# paddle a
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350,0)

# paddle b
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350,0)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.up()
pen.hideturtle()
pen.goto(0,260)
pen.write("Pavan : 0  Vaagmey : 0",align = 'center', font = ('courier',18,'normal'))


# define functions for paddle movements
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# key bindinds
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

while True:
    wn.update()
    
    #set the ball moving

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # set the ball bounce off the walls
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('*',winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('*', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pavan_score += 1
        winsound.PlaySound("pavan_win.WAV",winsound.SND_ASYNC)
        pen.write("Pavan : {}  Vaagmey : {}".format(pavan_score,vaagmey_score),align = 'center', font = ('courier',18,'normal'))

    if ball.xcor() <- 390:
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        vaagmey_score += 1
        winsound.PlaySound("vaagmey_win.WAV",winsound.SND_ASYNC)
        pen.write("Pavan : {}  Vaagmey : {}".format(pavan_score,vaagmey_score),align = 'center', font = ('courier',18,'normal'))

    # bounce the ball off paddles
    if (ball.xcor() >340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ) :
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() <-340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ) :
        ball.setx(-340)
        ball.dx *= -1
