import turtle
import os

window = turtle.Screen()
window.title("Game 1")
window.bgcolor(0, 0, 0)
window.setup(width = 1000, height = 1000)
window.tracer(5) #This function is used to turn turtle animation on or off and set a delay for update drawings.
window.update()

# Score
score_a = 0
score_b = 0

#PADDDLE A
paddle_A = turtle.Turtle()
paddle_A.speed(0) #Speed of animation, NOT paddle. 'fastest' : 0 'fast' : 10 'normal' : 6 'slow' : 3 'slowest' : 1
                    # speeds from 1 to 10 enforce increasingly faster animation of line drawing and turtle turning.
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.penup() #Pull the pen up – no drawing when moving. Because by default it would draw a line when moving
paddle_A.goto(-450, 0)
paddle_A.shapesize(stretch_wid = 5, stretch_len = 1)  #Paddle size. Default is 20pxl wide by 20pxl high
                                                        #5x20=100 1x20=20 so 100pxl high by 5pxl wide

#PADDLE B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.penup()
paddle_B.goto(450, 0)
paddle_B.shapesize(stretch_wid = 5, stretch_len = 1)

#BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1 #Ball will move by 2 pixels horizontally
ball.dy = 1 #Ball will move by 2 pixels vertically

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

def A_ymove_u():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def A_ymove_d():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def B_ymove_u():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)


def B_ymove_d():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

window.listen()  #It listen to a keyboard input
window.onkeypress(A_ymove_u, "w")
window.onkeypress(A_ymove_d, "s")
window.onkeypress(B_ymove_u, "Up")
window.onkeypress(B_ymove_d, "Down")


# def main():
while True:
    window.update() #Perform a TurtleScreen update. To be used when tracer is turned off.
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    # Top and bottom
    if ball.ycor() > 490:
        ball.sety(490)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    elif ball.ycor() < -490:
        ball.sety(-490)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_A.ycor() + 50 and ball.ycor() > paddle_A.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddle_B.ycor() + 50 and ball.ycor() > paddle_B.ycor() - 50:
        ball.dx *= -1
        os.system("afplay bounce.wav&")




# if __name__ == "__main__":
#     main()
