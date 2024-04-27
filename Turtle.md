# 🐢Turtle Graphics in Python
 A Turtle graphics toolkit provides a simple and enjoyable way to draw pictures in a window and gives you an opportunity to run several methods with an object. In the next few sections, we use Python’s turtle module to illustrate various features of object-based programming.

# Turtle Methods

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>t.speed(speed_level)</code></td>
      <td>Sets the drawing speed of t. The value of <code>speed_level</code> can be an integer between 0 and 10, where 0 is the fastest and 10 is the slowest.</td>
    </tr>
    <tr>
      <td><code>t.color(color1, color2)</code></td>
      <td>Sets the pen color of t to <code>color1</code> and the fill color to <code>color2</code>. If only one color is provided, it sets both the pen and fill color to that value.</td>
    </tr>
    <tr>
      <td><code>t.begin_fill()</code></td>
      <td>Starts filling the shape drawn from this point onwards with the current fill color.</td>
    </tr>
    <tr>
      <td><code>t.end_fill()</code></td>
      <td>Stops filling the shape. It is important to call this method after <code>begin_fill()</code> to actually fill the shape.</td>
    </tr>
    <tr>
      <td><code>t.pensize(pixels)</code></td>
      <td>Sets the width of t's pen to <code>pixels</code> pixels.</td>
    </tr>
    <tr>
      <td><code>t.pendown()</code></td>
      <td>Puts t's pen down, allowing it to draw on the canvas.</td>
    </tr>
    <tr>
      <td><code>t.penup()</code></td>
      <td>Picks t's pen up, allowing it to move without drawing on the canvas.</td>
    </tr>
    <tr>
      <td><code>t.goto(x, y)</code></td>
      <td>Moves t to the coordinates (<code>x</code>, <code>y</code>) on the canvas.</td>
    </tr>
    <tr>
      <td><code>t.circle(radius)</code></td>
      <td>Draws a circle with the given radius.</td>
    </tr>
    <tr>
      <td><code>t.left(degrees)</code></td>
      <td>Turns t to the left by <code>degrees</code> degrees.</td>
    </tr>
    <tr>
      <td><code>t.right(degrees)</code></td>
      <td>Turns t to the right by <code>degrees</code> degrees.</td>
    </tr>
    <tr>
      <td><code>t.forward(distance)</code></td>
      <td>Moves t forward by <code>distance</code> units in its current direction.</td>
    </tr>
    <tr>
      <td><code>t.backward(distance)</code></td>
      <td>Moves t backward by <code>distance</code> units in its current direction.</td>
    </tr>
    <tr>
      <td><code>t.home()</code></td>
      <td>Moves t back to its starting position and direction.</td>
    </tr>
    <tr>
      <td><code>t.fillcolor(color)</code></td>
      <td>Sets the fill color of t to <code>color</code>.</td>
    </tr>
    <tr>
      <td><code>t.pencolor(color)</code></td>
      <td>Sets the pen color of t to <code>color</code>.</td>
    </tr>
    <tr>
      <td><code>t.width(pixels)</code></td>
      <td>Sets the width of t's pen to <code>pixels</code>
