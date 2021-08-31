# Ensure the lunar mosaic is in the same location as this python file when called
# Use the following command on linux/Google Colab to download the mosaic
# wget -P . https://planetarymaps.usgs.gov/mosaic/Lunar_LRO_LROC-WAC_Mosaic_global_100m_June2013.tif

import pandas as pd
import numpy as np
from tifffile import imread
from PIL import Image
import os
import math
from PIL import Image
import pandas
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import platform

slash = "/"
if platform.system().lower() == 'windows':
    slash = "\\"

filename = "LROC"
im = imread("Lunar_LRO_LROC-WAC_Mosaic_global_100m_June2013.tif")
data = pandas.read_csv("lunar_crater_database_robbins_2018.csv")
lat = data["LAT_CIRC_IMG"]
lon = data["LON_CIRC_IMG"]
crop_im = im[int(len(im)/3):int(len(im)*2/3)]
ppd = 303.2334 # pixel per degree

lat_max = 90 - len(im)/3/ppd
lat_min = 90 - len(im)*2/3/ppd
lon_max = 360
lon_min = 0

os.system('mkdir dataset_lunar')
os.system('mkdir dataset_lunar' + slash + 'images')
os.system('mkdir dataset_lunar' + slash + 'labels')

small_dim = 593 # small image dimension
filename = "LROC"
for i in range(30):
    for j in range(180):
        x1 = small_dim * j
        x2 = small_dim * (j+1)
        y1 = small_dim * i
        y2 = small_dim * (i+1)
        small_im = Image.fromarray(crop_im[y1:y2,x1:x2])

        # region of small grid in lon lat
        grid_lat_min = lat_max - (i + 1) * small_dim/ppd # the zero is index
        grid_lat_max = grid_lat_min + small_dim/ppd
        grid_lon_min = j * small_dim/ppd
        grid_lon_max = grid_lon_min + small_dim/ppd

        craters = data[(lat <= grid_lat_max) & (lat >= grid_lat_min) & (lon <= (180+grid_lon_max)) & (lon >= (180+grid_lon_min))]
        craters_lat = craters["LAT_CIRC_IMG"]
        craters_lon = craters["LON_CIRC_IMG"]
        craters_w = craters["DIAM_ELLI_MAJOR_IMG"]
        craters_h = craters["DIAM_ELLI_MINOR_IMG"]
        craters_lat = craters_lat.to_numpy()
        craters_lon = craters_lon.to_numpy()
        craters_w= craters_w.to_numpy() * 10 / np.cos(craters_lat*np.pi/180) / small_dim
        craters_h= craters_h.to_numpy() * 10 / small_dim

        xx = (craters_lon - (180+grid_lon_min))/(small_dim/ppd)
        yy = (grid_lat_max - craters_lat)/(small_dim/ppd)
        text = ""
        for k in range(len(xx)):
            x0, y0 = max(0, xx[k] - 0.5*craters_w[k]), max(0, yy[k] - 0.5*craters_h[k])
            x1, y1 = min(1, xx[k] + 0.5*craters_w[k]), min(1, yy[k] + 0.5*craters_h[k])
            area = craters_w[k] * craters_h[k]
            area_inbox = (x1 - x0) * (y1 - y0)

            if area_inbox/area > 0.5:
                z1 = (x0 + x1)/2
                z2 = (y0 + y1)/2
                z3 = x1 - x0
                z4 = y1 - y0
                text += ("0" + " " + str(z1) + " " + str(z2) + " " + str(z3) + " " + str(z4) + "\n")

        if len(text) > 0:
            f = open("dataset_lunar" + slash + "labels" + slash + filename + "_%i_%i.txt" %(i, j), "w")
            f.write(text)
            f.close
            small_im.save("dataset_lunar" + slash + "images" + slash + filename + "_%i_%i.png" %(i, j))

os.system('cd ../')
