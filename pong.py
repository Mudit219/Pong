import turtle
import os
import time
import random
#Screen
import turtle
import concurrent.futures
import threading

def make_button_horz(button,size):
    button.begin_fill()
    for i in range(2):
        button.forward(size)
        button.left(90)
        button.forward(size/2)
        button.left(90)
    button.end_fill()

def make_button_vert(button,size):
    button.begin_fill()
    for i in range(2):
        button.forward(size/2)
        button.left(90)
        button.forward(size)
        button.left(90)
    button.end_fill()


def click(x,y):
    # print(x,y)
    if(x > 250 and x < 350 and y < -200 and y > -250):
        global start
        win.clear()
        start = False
        # time.sleep(1)

    if(x > -200 and x < -100 and y > 0 and y < 50):
        global index,rounds
        choice1 = turtle.Turtle()
        choice1.color("white","white")
        choice1.penup()
        choice1.hideturtle()
        choice1.goto(-190,-50)
        make_button_vert(choice1,45)
        
        choice2 = turtle.Turtle()
        choice2.color("white","white")
        choice2.penup()
        choice2.hideturtle()
        choice2.goto(-160,-50)
        make_button_vert(choice2,45)
        
        choice3 = turtle.Turtle()
        choice3.color("white","white")
        choice3.penup()
        choice3.hideturtle()
        choice3.goto(-130,-50)
        make_button_vert(choice3,45)
        
        index.goto(-178,-50)
        index.color("black")
        index.write("5",align="center",font=("Arial",16,"bold"))

        index.goto(-148,-50)
        index.color("black")
        index.write("10",align="center",font=("Arial",16,"bold"))
    
        index.goto(-118,-50)
        index.color("black")
        index.write("20",align="center",font=("Arial",16,"bold"))

    if(x > -190 and x < -170 and y > -50 and y < -5):
        rounds = 5
        index.goto(-178,-50)
        index.color("orange")
        index.write("5",align="center",font=("Arial",16,"bold"))

        index.goto(-148,-50)
        index.color("black")
        index.write("10",align="center",font=("Arial",16,"bold"))

        index.goto(-118,-50)
        index.color("black")
        index.write("20",align="center",font=("Arial",16,"bold"))


    if(x > -160 and x < -140 and y > -50 and y < -5):
        rounds = 10
        index.goto(-178,-50)
        index.color("black")
        index.write("5",align="center",font=("Arial",16,"bold"))

        index.goto(-148,-50)
        index.color("orange")
        index.write("10",align="center",font=("Arial",16,"bold"))

        index.goto(-118,-50)
        index.color("black")
        index.write("20",align="center",font=("Arial",16,"bold"))

    if(x > -130 and x < -110 and y > -50 and y < -5):
        rounds = 20
        index.goto(-178,-50)
        index.color("black")
        index.write("5",align="center",font=("Arial",16,"bold"))

        index.goto(-148,-50)
        index.color("black")
        index.write("10",align="center",font=("Arial",16,"bold"))

        index.goto(-118,-50)
        index.color("orange")
        index.write("20",align="center",font=("Arial",16,"bold"))

    ############################# BALL_SPEED
    if(x > 200 and x < 300 and y > 0 and y < 50):
        global ball_speed
        choice1 = turtle.Turtle()
        choice1.color("white","white")
        choice1.penup()
        choice1.hideturtle()
        choice1.goto(210,-50)
        make_button_vert(choice1,45)
        
        choice2 = turtle.Turtle()
        choice2.color("white","white")
        choice2.penup()
        choice2.hideturtle()
        choice2.goto(240,-50)
        make_button_vert(choice2,45)
        
        choice3 = turtle.Turtle()
        choice3.color("white","white")
        choice3.penup()
        choice3.hideturtle()
        choice3.goto(270,-50)
        make_button_vert(choice3,45)
        
        index.goto(222,-50)
        index.color("black")
        index.write("S",align="center",font=("Arial",20,"bold"))

        index.goto(252,-50)
        index.color("black")
        index.write("M",align="center",font=("Arial",20,"bold"))
    
        index.goto(282,-50)
        index.color("black")
        index.write("F",align="center",font=("Arial",20,"bold"))

    if(x > 210 and x < 230 and y > -50 and y < -5):

        ball_speed = (1.5,1.5)
        index.goto(222,-50)
        index.color("orange")
        index.write("S",align="center",font=("Arial",20,"bold"))

        index.goto(252,-50)
        index.color("black")
        index.write("M",align="center",font=("Arial",20,"bold"))
    
        index.goto(282,-50)
        index.color("black")
        index.write("F",align="center",font=("Arial",20,"bold"))


    if(x > 240 and x < 260 and y > -50 and y < -5):
        ball_speed = (2,2)
        index.goto(222,-50)
        index.color("black")
        index.write("S",align="center",font=("Arial",20,"bold"))

        index.goto(252,-50)
        index.color("orange")
        index.write("M",align="center",font=("Arial",20,"bold"))
    
        index.goto(282,-50)
        index.color("black")
        index.write("F",align="center",font=("Arial",20,"bold"))

    if(x > 270 and x < 290 and y > -50 and y < -5):
        ball_speed = (2.5,2.5)
        index.goto(222,-50)
        index.color("black")
        index.write("S",align="center",font=("Arial",20,"bold"))

        index.goto(252,-50)
        index.color("black")
        index.write("M",align="center",font=("Arial",20,"bold"))
    
        index.goto(282,-50)
        index.color("orange")
        index.write("F",align="center",font=("Arial",20,"bold"))



start = True
win = turtle.Screen()
win.setup(width = 800, height = 600)
win.bgcolor("cyan")
rounds = 5
ball_speed = (1.5,1.5)

win.tracer(0)
game_start = turtle.Turtle()
game_start.penup()
game_start.hideturtle()
game_start.goto(250,-250)
game_start.pendown()
game_start.color("white","red")
make_button_horz(game_start,100)
# print(button.pos())

turn = turtle.Turtle()
turn.penup()
turn.hideturtle()
turn.goto(-200,0)
turn.pendown()
turn.color("white","red")
make_button_horz(turn,100)

speed_button = turtle.Turtle()
speed_button.penup()
speed_button.hideturtle()
speed_button.goto(200,0)
speed_button.pendown()
speed_button.color("white","red")
make_button_horz(speed_button,100)

index = turtle.Turtle()
index.penup()
index.hideturtle()
index.goto(300,-240)
index.color("black")
index.write("Play",align="center",font=("Arial",20,"bold italic"))

index.goto(-150,10)
index.color("black")
index.write("Points",align="center",font=("Arial",20,"bold italic"))

index.goto(250,10)
index.color("black")
index.write("Ball Speed",align="center",font=("Arial",14,"bold italic"))

win.listen()
win.onclick(click,1)
# win.onclick(no_of_turns,1)

while start:
    win.update()

#####################################################
# win = turtle.Screen() # Making a screen object
# GAMESCREEN
win.title("Pong")
win.bgcolor("cyan")
FULLSCREEN = (1920,1000)
WIDTH = FULLSCREEN[0]
HEIGHT = FULLSCREEN[1]
win.setup(FULLSCREEN[0],FULLSCREEN[1])
# WIDTH = 800
# HEIGHT = 600
# win.setup(800,600)
win.tracer(0)  # Comment it out and check
scoreA = 0
scoreB = 0
paddle_speed = 50
paddle_pos = WIDTH/2-WIDTH/20
paddle_lenth = 5
play = True
# Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("red")
paddle_A.shapesize(stretch_wid= paddle_lenth,stretch_len=1) # By default it is 20x20 pixel now it is 100x20
paddle_A.penup()  # try this, it will not display the drawing while moving. 
paddle_A.goto(-paddle_pos,0)

# Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("red")
paddle_B.shapesize(stretch_wid= paddle_lenth,stretch_len=1)
paddle_B.penup()  # try this, it will not display the drawing while moving. 
paddle_B.goto(paddle_pos,0)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("black")
Ball.penup()  # try this, it will not display the drawing while moving. 
Ball.goto(0,0)
# Ball.dx = 0.5 # the speed(pixel) by which we wonna move
# Ball.dy = 0.5
(Ball.dx,Ball.dy) = (0,0)

# Pen
pen = turtle.Turtle()  # This will be used to write on screen
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(0,260)
pen.write("Score A: {}   Score B: {}".format(scoreA,scoreB),False,"center",font=("Arial",22,"bold"))

# Pen2
pen2 = turtle.Turtle()
pen2.hideturtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.goto(0,0)

# Functions
def paddle_A_up():
    y = paddle_A.ycor()
    y += paddle_speed
    # for i in range(paddle_speed):
    #     y += 1
    paddle_A.sety(y)
    return y

def paddle_A_down():
    y = paddle_A.ycor()
    y -= paddle_speed
    paddle_A.sety(y)
    return y


def paddle_B_up():
    y = paddle_B.ycor()
    y += paddle_speed
    paddle_B.sety(y)
    return y


def paddle_B_down():
    y = paddle_B.ycor()
    y -= paddle_speed
    paddle_B.sety(y)
    return y

def endgame(scoreA,scoreB,rounds):
    if(scoreA == rounds and scoreB != rounds):
        pen2.write("Player A wins",align= "center",font=("Arial",30,"bold italic"))    
    if(scoreA != rounds and scoreB == rounds):
        pen2.write("Player B wins",align= "center",font=("Arial",30,"bold italic"))

def reset():
    if(Ball.xcor() == 0 and Ball.ycor() == 0):
        pen2.clear()
        time.sleep(0.8)
        rand = random.randint(0,1)
        if(rand == 0):
            Ball.dx *= -1
        else:
            Ball.dx *= 1
        
        (Ball.dx,Ball.dy) = ball_speed

def start_game():
    global Ball,ball_speed
    if(Ball.dx == 0 and Ball.dy ==0):
        (Ball.dx,Ball.dy) = ball_speed

# Keyboard
win.listen()
win.onkeypress(paddle_A_up,"w") # Which fun to call on which key
win.onkeypress(paddle_A_down,"s")
win.onkeypress(paddle_B_up,"Up")
win.onkeypress(paddle_B_down,"Down")
win.onkeypress(reset,"r")
win.onkeypress(start_game,"p")

# Main loop
while(play == True):

    win.update()  # Very important to write to continously diplay
    # print(ball_speed,rounds)
    # Movement of ball
    Ball.setx(Ball.xcor() + Ball.dx)  # This will move the ball
    Ball.sety(Ball.ycor() + Ball.dy)

    # Score
    if(scoreA == rounds or scoreB == rounds):
        endgame(scoreA,scoreB,rounds)
        scoreA = 0
        scoreB = 0
        Ball.goto(0,0)
        Ball.dx = 0
        Ball.dy = 0

    pen.clear() # Clears previously written things
    pen.write("Score A: {}   Score B: {}".format(scoreA,scoreB),False,"center",font=("Arial",22,"bold"))

    # Top and Bottom boundaries
    if(Ball.ycor() > HEIGHT/2-HEIGHT/100):
        Ball.dy *= -1
        os.system("aplay ./Sound/Bounce4.wav&")
    if(Ball.ycor() < -(HEIGHT/2-HEIGHT/100)):
        Ball.dy *= -1
        os.system("aplay ./Sound/Bounce4.wav&") # make sure to add & symbol otherwise it will lag

    # Right and Left boundaries
    if(Ball.xcor() > WIDTH/2-WIDTH/100):
        rand_y = random.randint(-(HEIGHT/2-HEIGHT/100),HEIGHT/2-HEIGHT/100)
        Ball.goto(0,rand_y)
        # time.sleep(0.5)
        rand = random.randint(0,1)
        if(rand == 0):
            Ball.dx *= -1
        else:
            Ball.dx *= 1
        scoreA +=1
        os.system("aplay ./Sound/Score2.wav&")
        
    if(Ball.xcor() < -(WIDTH/2-WIDTH/100)):
        rand_y = random.randint(-(HEIGHT/2-HEIGHT/100),HEIGHT/2-HEIGHT/100)
        Ball.goto(0,rand_y)
        # time.sleep(0.5)
        rand = random.randint(0,1)
        if(rand == 0):
            Ball.dx *= -1
        else:
            Ball.dx *= 1
        scoreB += 1
        os.system("aplay ./Sound/Score2.wav&")

    # Paddle and ball collisions
    if(Ball.xcor() > paddle_pos-20 and Ball.xcor() < paddle_pos and (Ball.ycor() < paddle_B.ycor() + ((paddle_lenth*10)+3) and Ball.ycor() > paddle_B.ycor() - ((paddle_lenth*10)+3))):
        Ball.setx(paddle_pos-20) # Vey Imp to wrtie otherwise glitches will come
        Ball.dx *= -1
        os.system("aplay ./Sound/Bounce4.wav&")


    if(Ball.xcor() < -paddle_pos+20 and Ball.xcor() > -paddle_pos and (Ball.ycor() < paddle_A.ycor() + ((paddle_lenth*10)+3) and Ball.ycor() > paddle_A.ycor() - ((paddle_lenth*10)+3))):
        Ball.setx(-paddle_pos+20) # Very Imp to wrtie otherwise glitches will come
        Ball.dx *= -1
        os.system("aplay ./Sound/Bounce4.wav&")
    
    