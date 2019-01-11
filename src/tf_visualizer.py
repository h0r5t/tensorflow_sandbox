from tkinter import *
from datasets import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
LABEL_COLORS = { 0:"#FF0000", 1:"#0000FF" }
DRAW_AXIS = False


def visualizeDataset(dataset):
    root = Tk()

    w = Canvas(root,
               width=CANVAS_WIDTH,
               height=CANVAS_HEIGHT)
    w.pack()
    if DRAW_AXIS:
        x = int(CANVAS_WIDTH / 2)
        y = int(CANVAS_HEIGHT / 2)
        w.create_line(0, y, CANVAS_WIDTH, y, fill="#000000")
        w.create_line(x, 0, x, CANVAS_HEIGHT, fill="#000000")

    for (x, y), label in dataset.getPoints().items():
        x, y = translateToScreen(x, y, dataset.space_width)
        w.create_oval(x, y, x+5, y+5, fill=LABEL_COLORS[label])

    mainloop()


def translateToScreen(x, y, space_width):
    x = (x * CANVAS_WIDTH / space_width) + (CANVAS_WIDTH / 2)
    y = (y * CANVAS_HEIGHT / space_width) + (CANVAS_HEIGHT / 2)
    return x, y


if __name__ == '__main__':
    # dataset = generateXORDataSet(300, 20, True)
    # visualizeDataset(dataset)

    clusters = [ClusterPoint(5, -7, 0), ClusterPoint(2, 6, 1), ClusterPoint(-6, -3, 1)]
    dataset = generateGaussDist(cluster_points=clusters, samples_per_cluster=200, variance=5, space_width=30, generateFloats=True)
    visualizeDataset(dataset)
