# Example from: https://www.kaggle.com/crawford/resize-and-save-images-as-hdf5-256x256

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

def proc_images():
    """
    Saves compressed, resized images as HDF5 datsets
    Returns
        data.h5, where each dataset is an image or class label
        e.g. X23,y23 = image and corresponding class label
    """
    start = dt.datetime.now()
    # ../input/
    PATH = os.path.abspath(os.path.join('.', 'data'))
    # .
    SOURCE_IMAGES = os.path.join(PATH, "/")
    # ../imgs/*.png
    images = glob(os.path.join(SOURCE_IMAGES, "*.jpg"))
    # Load labels
    labels = pd.read_csv('./data/coinlabels.csv')
    #print(labels)  
    print(images)
    
    # Size of data
    NUM_IMAGES = len(images)
    HEIGHT = 3024//4
    WIDTH = 4032//4
    CHANNELS = 3
    SHAPE = (HEIGHT, WIDTH, CHANNELS)
    
    with h5py.File('data.h5', 'w') as hf: 
      for i,img in enumerate(images):            
          # Images
          image = io.imread(img)
          image = resize(image, (WIDTH,HEIGHT),  anti_aliasing=True)
          imgs = hf.create_dataset(
              name='coins',
              data=image,
              shape=(HEIGHT, WIDTH, CHANNELS),
              maxshape=(HEIGHT, WIDTH, CHANNELS),
              compression="gzip",
              compression_opts=9)
          end=dt.datetime.now()
          #print("\r", i, ": ", (end-start).seconds, "seconds", end="")
            
    #   # Labels
    #   print(labels.shape)
    #   lbls = hf.create_dataset(
    #       name='labels',
    #       shape= labels.shape,
    #       maxshape=labels.shape,
    #       compression="gzip",
    #       compression_opts=9)            
    #   lbls = labels

proc_images()

