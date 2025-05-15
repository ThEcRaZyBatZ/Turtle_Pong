import time,sys
from turtle import Turtle,bye

class MakePaddle:
    def __init__(self, a, b, screen):
        self.xval = a
        self.yval = b
        self.my_screen = screen
        self.paddle = Turtle("square")
        self.place_paddle()
        self.moving_up = False
        self.moving_down = False

    def place_paddle(self):
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.setheading(90)
        self.paddle.shapesize(stretch_wid=2, stretch_len=5)
        self.paddle.goto(self.xval, self.yval)

    def if_key_pressed_for_up(self):
        self.moving_up = True

    def if_key_pressed_for_down(self):
        self.moving_down = True

    def if_key_released_for_up(self):
        self.moving_up = False

    def if_key_released_for_down(self):
        self.moving_down = False

    def check_movement(self):
        if self.moving_up:
            self.move_paddle_up()
        if self.moving_down:
            self.move_paddle_down()
        self.my_screen.ontimer(self.check_movement, 20)

    def move_paddle_up(self):
        self.paddle.forward(10)

    def move_paddle_down(self):
        self.paddle.backward(10)
class Ball:
    def __init__(self,screen,paddle1,paddle2,scoreboard):
        self.ball=Turtle("circle")
        self.x_vel=1.3
        self.y_vel=1
        self.initial_ball()
        self.my_screen=screen
        self.scoreboard = scoreboard
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.left_points=0
        self.right_points=0

    def initial_ball(self):
        self.ball.color("white")
        self.ball.penup()

    def move_ball(self):
        self.ball.forward(self.x_vel)
        self.ball.setheading(90)
        self.ball.forward(self.y_vel)
        self.ball.setheading(0)

    def check_collision(self):
        if (self.ball.distance(self.paddle1) < 60 and self.ball.xcor() > 540):
            self.x_vel *= -1
            self.ball.setx(self.ball.xcor() - 20)
        elif (self.ball.distance(self.paddle2) < 60 and self.ball.xcor() < -540):
            self.x_vel *= -1
            self.ball.setx(self.ball.xcor() + 20)
        if self.ball.ycor() > 390 or self.ball.ycor() < -390:
            self.y_vel*= -1
        if self.ball.xcor() > 600:
            self.ball.goto(0, 0)
            self.x_vel=-1
            self.y_vel=1
            self.my_screen.ontimer(self.reset_ball,1200)
            self.scoreboard.player2_scores()
            return
        if  self.ball.xcor() < -600:
            self.x_vel = 1
            self.y_vel = 1
            self.ball.goto(0, 0)
            self.my_screen.ontimer(self.reset_ball, 1200)
            self.scoreboard.player1_scores()
            return
        self.move_ball()
        self.my_screen.ontimer(self.check_collision, 2)  # controls the speed of the ball

    def reset_ball(self):
        self.my_screen.update()
        self.check_collision()
class Scoreboard:
    def __init__(self,my_screen):
        self.score1 = 0
        self.score2 = 0
        self.pen = Turtle()
        self.pen.color("white")
        self.pen.penup()
        self.my_screen=my_screen
        self.pen.hideturtle()
        self.pen.goto(0, 360)
        self.update_score()

    def update_score(self):
        self.pen.clear()
        self.pen.write(f"{self.score2}     SCORE     {self.score1}", align="center", font=("Courier", 24, "bold"))

    def player1_scores(self):
        self.score1 += 1
        if self.score1==5:
            self.game_over("Player 2")
            return
        self.update_score()

    def player2_scores(self):
        self.score2 += 1
        if self.score2 == 5:
            self.game_over("Player 1")
            return
        self.update_score()
        #sup krupa <3


    def game_over(self,val):
        self.my_screen.clearscreen()
        self.my_screen.bgcolor("black")
        self.my_screen.tracer(0)
        pen = Turtle()
        pen.hideturtle()
        pen.color("red")
        pen.penup()
        pen.goto(0, 30)
        time.sleep(0.5)
        pen.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
        pen.goto(0, -30)
        pen.write(f"{val} WINS", align="center", font=("Arial", 40, "bold"))
        self.my_screen.update()
        time.sleep(2)
        bye()
        sys.exit()

def draw_dotted_line():
    temp_turtle = Turtle()
    temp_turtle.pensize(7)
    temp_turtle.color("white")
    temp_turtle.hideturtle()
    temp_turtle.penup()
    temp_turtle.goto(0, 350)
    temp_turtle.setheading(270)
    flag = False
    while temp_turtle.ycor() > -350:
        temp_turtle.forward(32)
        if 90 > temp_turtle.ycor() > -30:
            temp_turtle.penup()
        elif flag:
            temp_turtle.penup()
        else:
            temp_turtle.pendown()
        flag = not flag
