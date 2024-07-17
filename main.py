from turtle import Turtle, Screen
from pallete import Pallete
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width = 800, height = 600)
screen.tracer(0)


left_pallate = Pallete((-350, 0))
left_pallate.move_left()

right_pallete = Pallete((350, 0))
right_pallete.move_right()

score = Scoreboard()

ball = Ball()

# while loop for running the game continuosly
game_on = True

while game_on == True:
  time.sleep(ball.move_speed)
  ball.move()

  score.update_scoreboards()

  # detect collision with the top and bottom wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # detect collision with the pallate 
  if ball.distance(right_pallete) < 50 and ball.xcor() > 330 or ball.distance(left_pallate) < 50 and ball.xcor() < -330:
    ball.bounce_x()

   
  # if the right pallate misses the ball
  if ball.xcor() > 380:
    ball.reset_position()
    score.l_score += 1

  # if the left pallate misses the ball
  if ball.xcor() < -380:
    ball.reset_position()
    score.r_score += 1

  
  screen.update()


















screen.exitonclick()