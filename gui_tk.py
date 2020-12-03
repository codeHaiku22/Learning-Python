#!/usr/bin/python3
"""
Note: When running this code page (gui_tk.py) on WSL/2, ensure the following:
(1) sudo apt install python3-tk
(2) Download and install Xming X Server for Windows: https://sourceforge.net/projects/xming/?source=typ_redirect
(3) Add the line export DISPLAY=:0; to ~/.bashrc.
(4) Restart WSL/2.
(4) In the terminal run this file as follows: python -i gui_tk.py
       OR
    Add the line window.mainloop() within this file and run as follows: ./gui_tk.py
"""

#Working with Widgets
#Widgets are the building blocks of the Python GUI framework known as Tkinter.
#Each Widget is defined by a class.
"""
Button          Allows for basic user interaction
Canvas          Used to draw plots and graphs upon; can also be used to display images
CheckButton     Allows for a predefined set of options to be selected or de-selected
ComboBox        Presents a drop-down list of options and displays them one at a time
Entry           Takes input from the user in a single line of text
Frame           Outlines the frame of a window with a fixed size; windows require a frame to support them and give them structure
Label           Displays simple lines of text; can also be usd to display images
ListBox         Displays a list of ooptions for the user to select; all options are presented in one go
Menu            Used to create various types of menus
MenuButton      A combination of the button and menu widgets that displays a drop-down meny with a list of options once clicked; can use check buttons and radio buttons
RadioButton     Allows for a user to select only one of a predefined set of mutually exclusive options
Scale           Implements a graphical slider giving the user the option of picking through a range of values; the maximum and minimum values can be programtically defined
Scrollbar       Allows for scrolling from within a Window; enables scrolling for certain other widgets
Toplevel        Allows for the easy spawning of new Windows; a better alternative to spawning extra windows by using tk()
"""
import tkinter as tk

#Creating an Empty Window
window = tk.Tk()

#Adding a Widget

#create a label widget
greeting = tk.Label(text="Hello, Tkinter!")

#add it to the window
greeting.pack()

#Attributes of a widget can be changed accordingly
label1 = tk.Label(
    text="Hello, Tkinter!",
    foreground="white",
    background="#000000",
    width=25,
    height=5
)
label1.pack()

#Width and heighth are measured in text units.
# - One horizontal unit is measured by the width of the character "0"
# - One vertical unit is measured by the heighth of the character "0"
# - The width and height are relative to the default font on a user's machine.
#    + This ensures that the text fits properly in labels and buttons, no matter where the application is running.
label2 = tk.Label(text="Hello, Tkinter!", fg="black", bg="yellow", height=2, width=25)
label2.pack()

#A Tkinter button is simply a label that can be clicked.
button = tk.Button(text="Click me!", width=15, height=2, fg="black", bg="silver")
button.pack()

#The Tkinter entry allows us to capture user input.
#Entry widgets have 3 main operations:
# (1) .get()     Retrieves text
# (2) .delete()  Deletes text 
# (3) .insert()  Inserts text
entry = tk.Entry(fg="blue", bg="white", width=50)
entry.pack()

userInput = entry.get()
print(userInput)

#Tkinter Event Loop
#The code below tells Python to run the Tkinter event loop.
# - This method listens for events (button clicks, key presses) and blocks any code that comes after it from running until the window is closed.
window.mainloop()

print(userInput)
print("Really")
