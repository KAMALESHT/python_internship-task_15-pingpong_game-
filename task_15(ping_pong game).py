import turtle
#screen details
screen=turtle.Screen()
screen.title("|**PINGPONG** Game|")
screen.bgcolor("black")
screen.setup(width=1000,height=600)

#leftblock details

left_block=turtle.Turtle()
left_block.speed(0)
left_block.shape("square")
left_block.color("red")
left_block.shapesize(stretch_wid=7,stretch_len=2)
left_block.penup()
left_block.goto(-400,0)

#rightblock details

right_block=turtle.Turtle()
right_block.speed(0)
right_block.shape("square")
right_block.color("red")
right_block.shapesize(stretch_wid=7,stretch_len=2)
right_block.penup()
right_block.goto(400,0)

#ball details

ball=turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx=4
ball.dy=-4


#score details

PLAYER_LEFT= 0  #player on the left side
PLAYER_RIGHT= 0  #player on the right side


score=turtle.Turtle()
score.speed(0)
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0,250)
score.write("PLAYER_LEFT : 0     PLAYER_RIGHT : 0",
            align="center"  ,font=("Courier",26, "normal"))

#block_movement details

def blockL_up():
    y=left_block.ycor()
    y+=25
    left_block.sety(y)
def blockL_down():
    y=left_block.ycor()
    y-=25
    left_block.sety(y)
def blockR_up():
    y=right_block.ycor()
    y+=25
    right_block.sety(y)
def blockR_down():
    y=right_block.ycor()
    y-=25
    right_block.sety(y)

#keyboard key assignments
screen.listen()
screen.onkeypress(blockL_up,"q")
screen.onkeypress(blockL_down,"z")
screen.onkeypress(blockR_up,"Up")
screen.onkeypress(blockR_down,"Down")

while True:
    screen.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
        
    
    if ball.ycor()>280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor()>500:
        ball.goto(0,0)
        ball.dy*=-1
        PLAYER_LEFT+=1
        score.clear()
        score.write("PLAYER_LEFT : {}    PLAYER_RIGHT : {}".format(
                    PLAYER_LEFT,PLAYER_RIGHT),
            align="center"  ,font=("Courier",26, "normal"))

    if ball.xcor()<-500:
        ball.goto(0,0)
        ball.dy*=-1
        PLAYER_RIGHT+=1
        score.clear()
        score.write("PLAYER_LEFT : {}    PLAYER_RIGHT : {}".format(
                    PLAYER_LEFT,PLAYER_RIGHT),
            align="center"  ,font=("Courier",26, "normal"))

        #ball meets block

    if (ball.xcor()>360 and
                ball.xcor()<370) and(ball.ycor()<right_block.ycor()+40 and
                 ball.ycor()>right_block.ycor()-40):

                ball.setx(360)
                ball.dx*=-1
    if (ball.xcor()<-360 and
                ball.xcor()>-370) and(ball.ycor()<left_block.ycor()+40 and
                 ball.ycor()>left_block.ycor()-40):

                ball.setx(-360)
                ball.dx*=-1
        






