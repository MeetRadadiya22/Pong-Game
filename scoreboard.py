from turtle import Turtle

class Scoreboard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    

  def update_scoreboards(self):
    self.clear()
    self.goto(-100, 180)
    self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
    self.goto(100, 180)
    self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

