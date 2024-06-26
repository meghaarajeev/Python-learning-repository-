>>> from turtle import Turtle
>>> t=Turtle()
>>> t.speed(20)
>>> for i in range(100):
...  t.circle(5*i)
...  t.circle(-5*i)
...  t.left(i)
