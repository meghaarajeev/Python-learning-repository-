from turtle import Turtle
t=Turtle()
def hex(t, len):
   for i in range(6):
      t.forward(len)
      t.left(60)
hex(t,100)
