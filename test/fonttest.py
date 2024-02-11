##########################################################################
# Copyright (c) 2022-2024 Reinhard Caspary                               #
# <reinhard.caspary@phoenixd.uni-hannover.de>                            #
# This program is free software under the terms of the MIT license.      #
##########################################################################

from tkinter import Tk, Canvas
import time

from plotfont import Font

size = 50
frame = 0.3 * size
lw = 0.1*size

t = time.strftime("%H:%M:%S", time.localtime())
args = {
    "size": size,
    "width": size,
    "valign": "bottom",
    "mirrory": True,
    }
font = Font(**args)
lines = font.string("%s - Hello World!" % t, frame, frame)
bbox = font.bbox(lines)

win = Tk()
width = bbox[2]-bbox[0] + 2*frame
height = bbox[3]-bbox[1] + 2*frame
canvas = Canvas(win, width=width, height=height)
print("Canvas width:  %d px" % width, height)    
print("Canvas height: %d px" % height)    

for line in lines:
    for i in range(len(line)-1):
        x0, y0 = line[i]
        x1, y1 = line[i+1]
        if x0 == x1 and y0 == y1:
            x0 -= 0.5*lw
            y0 -= 0.5*lw
            x1 += 0.5*lw
            y1 += 0.5*lw
            canvas.create_oval(x0, y0, x1, y1, outline="", fill="red")
        else:
            canvas.create_line(x0, y0, x1, y1, capstyle="round", fill="red", width=lw)
        #print(x0, y0, x1, y1)
canvas.pack()

win.mainloop()
print("Done.")
