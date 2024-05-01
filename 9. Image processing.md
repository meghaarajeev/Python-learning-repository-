# Image Processing 🤳🏼

Image processing in Python involves manipulating digital images using libraries like OpenCV, Pillow, and scikit-image. It includes tasks such as loading, enhancing, filtering, transforming, and analyzing images. These libraries provide powerful tools for tasks like image enhancement, feature extraction, object detection, segmentation, and analysis, making Python a popular choice for image-related applications in various domains.

# Properties of Images 

- When an image is loaded into a program such as a Web browser, the software maps the 
bits from the image file into a rectangular area of colored pixels for display. 
- The coordinates of the pixels in this two-dimensional grid range from (0, 0) at the upper-left corner 
of an image to (width – 1, height – 1) at the lower-right corner, where width and height are 
the image’s dimensions in pixels. 
- The screen coordinate system for the display of an 
image is somewhat different from the standard Cartesian coordinate system that we used 
with Turtle graphics, where the origin (0, 0) is at the center of the rectangular grid. 
- The RGB color system introduced earlier in this chapter is a common way of representing the 
colors in images. For our purposes, then, an image consists of a width, a height, and a set 
of color values accessible by means of (x, y) coordinates. A color value consists of the tuple 
(r, g, b), where the variables refer to the integer values of its red, green, and blue 
components, respectively

# Image Methods

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>i = Image(filename)</td>
      <td>Loads and returns an image from a file with the given filename. Raises an error if the filename is not found or the file is not a GIF file.</td>
    </tr>
    <tr>
      <td>i = Image(width, height)</td>
      <td>Creates and returns a blank image with the given dimensions. The color of each pixel is transparent, and the filename is the empty string.</td>
    </tr>
    <tr>
      <td>i.getWidth()</td>
      <td>Returns the width of i in pixels.</td>
    </tr>
    <tr>
      <td>i.getHeight()</td>
      <td>Returns the height of i in pixels.</td>
    </tr>
    <tr>
      <td>i.getPixel(x, y)</td>
      <td>Returns a tuple of integers representing the RGB values of the pixel at position (x, y).</td>
    </tr>
    <tr>
      <td>i.setPixel(x, y, (r, g, b))</td>
      <td>Replaces the RGB value at the position (x, y) with the RGB value given by the tuple (r, g, b).</td>
    </tr>
    <tr>
      <td>i.draw()</td>
      <td>Displays i in a window. The user must close the window to return control to the method’s caller.</td>
    </tr>
    <tr>
      <td>i.clone()</td>
      <td>Returns a copy of i.</td>
    </tr>
    <tr>
      <td>i.save()</td>
      <td>Saves i under its current filename. If i does not yet have a filename, save does nothing.</td>
    </tr>
    <tr>
      <td>i.save(filename)</td>
      <td>Saves i under filename. Automatically adds a .gif extension if filename does not contain it.</td>
    </tr>
  </tbody>
</table>
