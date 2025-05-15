from Pong import MakePaddle,draw_dotted_line,Ball,Scoreboard
from turtle import Screen
my_screen=Screen()
my_screen.bgcolor("black")
my_screen.setup(1200, 800)
my_screen.tracer(0)

Paddle1=MakePaddle(580,0,my_screen)
Paddle2=MakePaddle(-580,0,my_screen)
scoreboard = Scoreboard(my_screen)
my_ball=Ball(my_screen,Paddle1.paddle,Paddle2.paddle,scoreboard)
draw_dotted_line()
my_screen.update()

my_screen.listen()
my_screen.onkeypress(fun=Paddle1.if_key_pressed_for_up,key="Up")
my_screen.onkeypress(fun=Paddle1.if_key_pressed_for_down,key="Down")
my_screen.onkeyrelease(fun=Paddle1.if_key_released_for_up,key="Up")
my_screen.onkeyrelease(fun=Paddle1.if_key_released_for_down,key="Down")

my_screen.onkeypress(fun=Paddle2.if_key_pressed_for_up,key="w")
my_screen.onkeypress(fun=Paddle2.if_key_pressed_for_down,key="s")
my_screen.onkeyrelease(fun=Paddle2.if_key_released_for_up,key="w")
my_screen.onkeyrelease(fun=Paddle2.if_key_released_for_down,key="s")
Paddle1.check_movement()
Paddle2.check_movement()
my_screen.ontimer(my_ball.check_collision,2000)
try:
    while True:
        my_screen.update()
except:
    pass
my_screen.exitonclick()
