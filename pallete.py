from turtle import Turtle, Screen




class Pallete(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square") 
    self.color("white")
    self.shapesize(5, 1)
    self.penup()
    self.goto(position)
    
    
    

  def move_left(self):
    screen = Screen()
    screen.listen()

    screen.onkeypress(fun = self.up, key = "w")
    screen.onkeypress(fun = self.down, key = "s")


  def move_right(self):
    screen = Screen()
    screen.listen()

    screen.onkeypress(fun = self.up, key = "Up")
    screen.onkeypress(fun = self.down, key = "Down")
    

  def up(self):
    newY = self.ycor() + 20
    self.teleport(x = self.xcor(), y = newY)
    
  def down(self):
    newY = self.ycor() - 20
    self.teleport(x = self.xcor(), y = newY)
 