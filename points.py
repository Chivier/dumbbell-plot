from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import numpy as np

im = Image.open("plot.png")
pix = im.load()

colors = [
    (254, 254, 254),
    (28, 25, 26),
    (140, 139, 137),
    (34, 163, 207),
    (249, 219, 127),
]

dots_on_plot = []
for x_index in range(im.size[0]):
    for y_index in range(im.size[1]):
        r, g, b, a = pix[x_index, y_index]
        # check color
        color_dist = 255 * 3
        color_similar = None
        for color_item in colors:
            cr, cg, cb = color_item
            if (abs(cr - r) + abs(cg - g) + abs(cb - b)) < color_dist:
                color_dist = abs(cr - r) + abs(cg - g) + abs(cb - b)
                color_similar = color_item
        if color_similar != colors[4]:
            continue
        dots_on_plot.append((x_index, y_index))


# print(dots_on_plot)
# print(len(dots_on_plot))

x_ave = 0
y_ave = 0
for dot in dots_on_plot:
    x, y = dot
    x_ave += x
    y_ave += y
x_ave /= len(dots_on_plot) * 1.0
y_ave /= len(dots_on_plot) * 1.0
x_ave, y_ave = int(x_ave), int(y_ave)

for index in range(len(dots_on_plot)):
    x, y = dots_on_plot[index]
    dots_on_plot[index] = (x - x_ave, y - y_ave)


fig, ax = plt.subplots()
ax.plot([x for (x, y) in dots_on_plot], [y for (x, y) in dots_on_plot], "k")
ax.set(aspect=1)
