import tkinter
from datasets import *
import colorsys
import numpy as np

CANVAS_SIZE = 800
LABEL_COLORS = { -1:"#FF0000", 1:"#0000FF" }
DRAW_AXIS = True


def visualizeDataset(dataset):
    root = tkinter.Tk()

    w = tkinter.Canvas(root,
               width=CANVAS_SIZE,
               height=CANVAS_SIZE)
    w.pack()
    if DRAW_AXIS:
        x = int(CANVAS_SIZE / 2)
        y = int(CANVAS_SIZE / 2)
        w.create_line(0, y, CANVAS_SIZE, y, fill="#1B2021")
        w.create_line(x, 0, x, CANVAS_SIZE, fill="#1B2021")

    for (x, y), label in dataset.getPoints().items():
        x, y = translateToScreen(x, y, dataset.space_width)
        w.create_oval(x, y, x+5, y+5, fill=LABEL_COLORS[label])

    tkinter.mainloop()


def visualizeClassification(tf_model, dataset):
    print("\nPreparing classifier visualization...")
    space_width = dataset.space_width
    delta = 0.25
    delta_translated = CANVAS_SIZE / (space_width / delta)

    root = tkinter.Tk()
    w = tkinter.Canvas(root,
               width=CANVAS_SIZE,
               height=CANVAS_SIZE)
    w.pack()

    x = -space_width/2
    y = -space_width/2
    while x < space_width/2:
        while y < space_width/2:
            prediction = tf_model.predict(np.expand_dims([x, y], 0))[0][0]
            if prediction < 0:
                color = interpolateColor((255, 0, 0), 1+prediction)
            else:
                color = interpolateColor((0, 0, 255), 1-prediction)
            xt, yt = translateToScreen(x, y, space_width)
            w.create_rectangle(xt, yt, xt+delta_translated, yt+delta_translated, fill=color, width=0)
            y += delta
        y = -space_width/2
        x += delta

    for (x, y), label in dataset.getPoints().items():
        x, y = translateToScreen(x, y, dataset.space_width)
        w.create_oval(x, y, x+5, y+5, fill=LABEL_COLORS[label])

    tkinter.mainloop()


def interpolateColor(color_tupel, percent):
    r = int(color_tupel[0] + percent * (255 - color_tupel[0]))
    g = int(color_tupel[1] + percent * (255 - color_tupel[1]))
    b = int(color_tupel[2] + percent * (255 - color_tupel[2]))

    r = max(min(r, 255), 0)
    g = max(min(g, 255), 0)
    b = max(min(b, 255), 0)

    hex_code = '#%02x%02x%02x' % (r, g, b)
    return hex_code


def translateToScreen(x, y, space_width):
    x = (x * CANVAS_SIZE / space_width) + (CANVAS_SIZE / 2)
    y = (y * CANVAS_SIZE / space_width) + (CANVAS_SIZE / 2)
    return x, y
