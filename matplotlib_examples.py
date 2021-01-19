#!/usr/bin/python3

#Matplotlib
"""
Matplotlib is a low-level graph plotting library in Python that serves as a visualization utility.
It was crated by John D. Hunter and is open-source.
Matplotlib is mostly written in Python, a few segments are written in C, Objective-C, and JavaScript for platform compatibility.
"""

#---[ Install Pandas ]---------------------------------------------------------------------------------------------------------------------------------

#Matplotlib can be installed using the command: pip install matplotlib
#python -m pip install matplotlib
#Collecting matplotlib
#  Using cached matplotlib-3.3.3-cp38-cp38-manylinux1_x86_64.whl (11.6 MB)
#Requirement already satisfied: cycler>=0.10 in ./.local/lib/python3.8/site-packages (from matplotlib) (0.10.0)
#Requirement already satisfied: kiwisolver>=1.0.1 in ./.local/lib/python3.8/site-packages (from matplotlib) (1.3.1)
#Requirement already satisfied: pillow>=6.2.0 in ./.local/lib/python3.8/site-packages (from matplotlib) (8.0.1)
#Requirement already satisfied: python-dateutil>=2.1 in ./.local/lib/python3.8/site-packages (from matplotlib) (2.8.1)
#Requirement already satisfied: numpy>=1.15 in ./.local/lib/python3.8/site-packages (from matplotlib) (1.19.4)
#Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in ./.local/lib/python3.8/site-packages (from matplotlib) (2.4.7)
#Requirement already satisfied: six in /usr/lib/python3/dist-packages (from cycler>=0.10->matplotlib) (1.14.0)
#Installing collected packages: matplotlib
#Successfully installed matplotlib-3.3.3

import matplotlib

#Check Matplotlib version
print(matplotlib.__version__)                                               #3.3.3

#---[ Matplotlib Pyplot ]-----------------------------------------------------------------------------------------------------------------------------

#Most of Matplotlib lies under the pyplot submodule.

#Draw a line in a digram from position (0,0) to position (6,250)
import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([0, 6])
ypoints=np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

#---[ Matplotlib Plotting ]---------------------------------------------------------------------------------------------------------------------------

#Plotting x and y Points
"""
The plot() function is used to draw points (markers) in a diagram.
By default, the plot() function draws a line from point to point.
The function takes parameters for specifying points in the diagram.
 - Parameter 1 is an array containing the points on the x-axis.
 - Parameter 2 is an array containing the points on the y-axis.
"""

import matplotlib.pyplot as plt
import numpy as np

#Plotting with a Line

#Draw a line in a diagram from position (1,3) to position (8,10)
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

#Plotting Without a Line

#Draw 2 points in the diagram, one at position (1,3) and one in position (8,10)
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

#Multiple Points

#Draw a line in a diagram from position (1,3) to position (2,8), then to position (6,1), and finally to position (8,10)
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

#Default X-Points
#If we do not specify the points inthe x-axis, they will get the default values 0, 1, 2, 3, etc. (depending on the length of the y-points).
#So, we can use points from the example above and omit the x-points.

#Plotting without x-points
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

#---[ Matplotlib Markers ]----------------------------------------------------------------------------------------------------------------------------

#You can use the keyword argument "marker" to emphasize each point with a specified marker.

#Marker Reference
"""
Marker    Description
------    --------------
'o'       Circle 	
'*'       Star 	
'.'       Point 	
','       Pixel 	
'x'       X 	
'X'       X (filled) 	
'+'       Plus 	
'P'       Plus (filled) 	
's'       Square 	
'D'       Diamond 	
'd'       Diamond (thin) 	
'p'       Pentagon 	
'H'       Hexagon 	
'h'       Hexagon 	
'v'       Triangle Down 	
'^'       Triangle Up 	
'<'       Triangle Left 	
'>'       Triangle Right 	
'1'       Tri Down 	
'2'       Tri Up 	
'3'       Tri Left 	
'4'       Tri Right 	
'|'       Vline 	
'_'       Hline
"""

#Line Reference
"""
Line Syntax    Description
-----------    ------------------
'-'            Solid line 	
':'            Dotted line 	
'--'           Dashed line 	
'-.'           Dashed/dotted line
"""

#Color Reference
"""
Color Syntax    Description
------------    -----------
'r'             Red 	
'g'             Green 	
'b'             Blue 	
'c'             Cyan 	
'm'             Magenta 	
'y'             Yellow 	
'k'             Black 	
'w'             White
"""

import matplotlib.pyplot as plt
import numpy as np

#Mark each point with a circle
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

#Mark each point with a star
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = '*')
plt.show()

#Format String fmt
#You can also use the shortcut string notation parameter (fmt) to specify the marker using this syntax: marker|line|color
#If you leave out the line parameter, no line will be drawn.

#Mark each point with a red cirlce, using a red dotted line 
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

#Marker Size
#You can use the keyword argument markersize, or ms for short, to set the size of the markers.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

#Marker Edge Color
#You can use the keyword argument markeredgecolor, or mec for short, to set the color of the edge (outline) of the markers.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#Marker Face Color
#You can use the keyword argument markerfacecolor, or mfc for short, to set the fill color of the markers.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

#Marker Face Color and Marker Edge Color
#Set the color for both the edge and the face.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'g')
plt.show()

#Colors Using Hexadecimal Values
#Set the color for both the edge and the face.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()

#Colors Using Color Name
#A list of 140 color names can be found at https://www.w3schools.com/colors/colors_names.asp
#Set the color for both the edge and the face.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()

#---[ Matplotlib Line ]-------------------------------------------------------------------------------------------------------------------------------

#Line Reference
"""
Style                Abbreviated    Description
-----------------    -----------    ------------------
'solid' (default)    '-'            Solid line 	
'dotted;             ':'            Dotted line 	
'dashed'             '--'           Dashed line 	
'dashdot             ''-.'          Dashed/dotted line
'None'               '' or ' '      None/no line
"""

#You can use the keyword argument linestyle or ls to change the stule of the plotted line.

import matplotlib.pyplot as plt
import numpy as np

#Create a dotted line
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

#Create a dashed line
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

#Create a dotted line - abbreviated syntax
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = ':')
plt.show()

#Create a dashed line - abbreviated syntax
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = '--')
plt.show()

#Line Color
#You can use the keyword argument color of the shorter c to set the color of the line.

#Colors Using Color Name
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'red')
plt.show()

#Colors Using Abbreviated Color Name
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = 'r')
plt.show()

#Colors Using Hexadecimal Values
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, c = '#4CAF50')
plt.show()

#Line Width
#You can use the keyword argument linewidth or the shorter lw to change the width of the line.
# - The value is a floating number in points.

#Plot with a 20.5 point wide line.
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

#Multiple Lines
#You can plot as many lines as you like by simply adding more plt.plot() functions.

#Draw 2 lines by specifying a plt.plot() function for each line.
# - In this example, only the y-axis is being given values.  
# - The x-axis is defaulting to (0, 1, 2, 3).
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

#You can also plot many lines by adding the points for the x and y axis for each line in the same plt.plot() function.
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()

#---[ Matplotlib Subplots ]---------------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#Display Multiple Plots
#With the subplots() function, you can draw multiple plots in 1 figure.
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

#The subplots() Function
#subplots() takes 3 arguments:
# - Rows
# - Columns
# - Index of the current plot (which subplot to display in)

#Draw 2 plots on top of each other
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()

#You can draw as many plots as you like on 1 figure, just describe the rows, columns, and the index of the plot.
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

#plot 3:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

#plot 4:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

#plot 5:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

#plot 6:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

#Title
#You can add a title to each plot with the title() function.

#2 plots with titles
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()

#Super Title
#You can add a title to the entire figure with the suptitle() function.

#Add a title for the entire figure

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

#~~~[ Subheading ]~~~~~~~~~~~~~~~~~~~~~