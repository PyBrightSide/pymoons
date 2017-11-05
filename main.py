"""
	@brief Main start page
	@author Py.Brightside
"""
import sys
from tkinter import *
from tkinter import Button

def quit():
    """
        @brief print msg and quit from prog
        @author Py.Brightside
    """
    print('Hello, I must be going...')
    sys.exit()

root = Tk()

widget = Label(root)
widget.config(text='Hello GUI world!')
widget.pack(side=TOP, expand=YES, fill=BOTH)

bt1 = Button(None,
            text='Press',
            command=(lambda: print('Hello') or sys.exit()) )
bt1.pack(side=LEFT, expand=YES, fill=BOTH)

root.title('gui1g.py')
root.mainloop()
