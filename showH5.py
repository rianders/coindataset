from skimage import data, color, io
from skimage.transform import resize
import datetime as dt
import h5py
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np
import os
import pandas as pd
from glob import glob
import argparse
from tqdm import tqdm



LABEL_FILE = "./labeldata.h5"
DATA_H5_FILE = "./imagedata.h5"
DATA_FILE = "./dataimages.npz"

labels = pd.read_hdf(LABEL_FILE)
images = np.load(DATA_FILE)['images']
# print("data keys".format(data.keys()))
#print(data.keys())
print(images.shape)
#data['images']
print("images shape: {}".format(images.shape))
# with h5py.File(DATA_H5_FILE, 'r') as hf: 
#     print(list(hf.keys()))
#     print(hf['images'])
# hf.close()

# print(images.shape)
# row = images[0]
# row = np.zeros(row)
# row = np.empty_like(images[0])
# print("row shape: {}".format(row.shape))
# np.insert(images, row, images)
# dataset = list(zip(labels,images))
# print(dataset.shape)
# for i, row in enumerate(dataset):
#     print("{}{}".format(i, row))

plots = np.arange(0, 63)
nrows = 8
plot_cnt = len(plots) + 1
ncols = int(plot_cnt//nrows)
print("nrows:{} lenplots: {} ncols:{}".format(ncols, len(plots), nrows))
fig, ax2d = plt.subplots(nrows,ncols)
axarr = np.ravel(ax2d)
images[57]

print("ravel.shape:{}".format(axarr.shape))
for count, img in enumerate(images):
    #print("count:{}, img.shape:{}".format(count, img.shape))
    axarr[count].imshow(img)
plt.show()


