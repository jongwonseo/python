from turtle import Screen, Turtle # Turtle:거북이 모양등 정의

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
  
  def __init__(self):
    self.segments=[]
    self.create_snake()
    self.head = self.segments[0] #어디로 갈지
    
  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)
      
  def move(self):
    for seg_num in range(len(self.segments)-1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.segments[0].forward(MOVE_DISTANCE)
 
 
  def add_segment(self ,position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)
    
  def reset(self):
    for seg in self.segments:
      self.goto(1000,1000)
    self.segments.clear()
    self.create_snake()
    self.head - self.segments[0]
    
  def extend(self):
    self.add_segment(self.segments[-1].position())
  
  
  def up(self): # 위 키
    if self.head.heading() != DOWN:
      self.segments[0].setheading(UP)
  
  def down(self): # 아래 키
    if self.head.heading() != UP:
      self.segments[0].setheading(DOWN)

  def left(self): # 왼쪽 키
    if self.head.heading() != RIGHT:
      self.segments[0].setheading(LEFT)

  def right(self): # 오른쪽 키
    if self.head.heading() != LEFT:
      self.segments[0].setheading(0)
  
  