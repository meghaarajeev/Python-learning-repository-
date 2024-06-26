from turtle import Turtle
t=Turtle()
def hex(t, len):
   for i in range(6):
      t.forward(len)
      t.left(60)
def radhex(t,n,length):
  for i in range(n):
    hex(t,length)
    t.left(360/n)
radhex(t,30,100)
