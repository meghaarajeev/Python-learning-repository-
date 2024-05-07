# 🐢Turtle Graphics in Python
 A Turtle graphics toolkit provides a simple and enjoyable way to draw pictures in a window and gives you an opportunity to run several methods with an object. In the next few sections, we use Python’s turtle module to illustrate various features of object-based programming.

# Attributes of Turtle 
1. Heading : specified in degrees. A turtle is initially facing east 0 degree.
2. Colour : The initial colour black that can be changed to 16 million other colours.
3. Width : Width of the line drawn when the turtle moves. Initial width is 1 px.
4. Down : This can be either true or false and controls whether the turtles pen is up or down.

# Turtle Methods
| Method | Description |
|--------|-------------|
| `t.speed(speed_level)` | Sets the drawing speed of `t`. The value of `speed_level` can be an integer between 0 and 10, where 0 is the fastest and 10 is the slowest. |
| `t.color(color1, color2)` | Sets the pen color of `t` to `color1` and the fill color to `color2`. If only one color is provided, it sets both the pen and fill color to that value. |
| `t.begin_fill()` | Starts filling the shape drawn from this point onwards with the current fill color. |
| `t.end_fill()` | Stops filling the shape. It is important to call this method after `begin_fill()` to actually fill the shape. |
| `t.pensize(pixels)` | Sets the width of `t`'s pen to `pixels` pixels. |
| `t.pendown()` | Puts `t`'s pen down, allowing it to draw on the canvas. |
| `t.penup()` | Picks `t`'s pen up, allowing it to move without drawing on the canvas. |
| `t.goto(x, y)` | Moves `t` to the coordinates (`x`, `y`) on the canvas. |
| `t.circle(radius)` | Draws a circle with the given radius. |
| `t.left(degrees)` | Turns `t` to the left by `degrees` degrees. |
| `t.right(degrees)` | Turns `t` to the right by `degrees` degrees. |
| `t.forward(distance)` | Moves `t` forward by `distance` units in its current direction. |
| `t.backward(distance)` | Moves `t` backward by `distance` units in its current direction. |
| `t.home()` | Moves `t` back to its starting position and direction. |
| `t.fillcolor(color)` | Sets the fill color of `t` to `color`. |
| `t.pencolor(color)` | Sets the pen color of `t` to `color`. |
| `t.width(pixels)` | Sets the width of `t`'s pen to `pixels`. |

