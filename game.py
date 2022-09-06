import time
from turtle import Screen
from classes import Paddle, Ball, Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

p1 = Paddle((350, 0))
p2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p1.go_up, "Up")
screen.onkey(p1.go_down, "Down")
screen.onkey(p2.go_up, "w")
screen.onkey(p2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with up/down wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #detect collision with paddles
    if ball.distance(p1) < 50 and ball.xcor() > 320 or ball.distance(p2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect ball miss the p2_paddle
    if ball.xcor() > 380:
        ball.bounce_x()
        ball.home()
        scoreboard.p1_point()
        ball.move_speed = 0.1

    #detect ball miss the p1_paddle
    if ball.xcor() < -380:
        ball.bounce_x()
        ball.home()
        scoreboard.p2_point()
        ball.move_speed = 0.1


screen.exitonclick()
