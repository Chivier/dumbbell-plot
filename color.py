from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


def rgb_to_hex(rgb):
    return "%02x%02x%02x" % rgb


im = Image.open("plot.png")  # Can be many different formats.
pix = im.load()

colorset = list()
for x_index in range(im.size[0]):
    for y_index in range(im.size[1]):
        r, g, b, a = pix[x_index, y_index]
        colorset.append(np.array([r, g, b]))

colorset = np.array(colorset)

plt.imshow([colorset])
kmeans = KMeans(n_clusters=5, random_state=0).fit(colorset)
colorinfo = kmeans.cluster_centers_.astype(int)
print(colorinfo)
