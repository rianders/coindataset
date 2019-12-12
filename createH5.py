from skimage import data, color, io
from skimage.transform import resize
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.pylab as plb
import numpy as np
import os
import pandas as pd
import h5py
from glob import glob
import argparse
from tqdm import tqdm

def main():
    #This code sets up the parser for command line arguments specifying parameters for creating the h5py file.
    parser=argparse.ArgumentParser()
    parser.add_argument("data_f")
    parser.add_argument("label_f")
    parser.add_argument("-o","--output", action='store', default="data.h5", help='output data dir and filename')
    parser.add_argument("-f","--force", action='store_false', help="overwrite output file")
    args=parser.parse_args()

    OUTPUT_FILE = args.output
    DATA_DIR = args.data_f
    LABEL_FILE = args.label_f
    SOURCE_IMAGES = os.path.join(DATA_DIR)

    images = glob(os.path.join(SOURCE_IMAGES, "*.jpg"))
    labels = pd.read_csv(LABEL_FILE,na_values='-')
    #np.savez("asdfasdf",labels.to_numpy())
    labels.to_hdf("labeldata.h5", "labels",mode="w")
    #reread = pd.read_hdf('./labeldata.h5')  
    data = []
    
    print("d:{} lb:{} of:{} img:{}".format(args.data_f, args.label_f, OUTPUT_FILE, images))
    print("{}".format(labels.to_numpy()[0]))
    #if path.isfile(OUTPUT_FILE) and args.force:

    #  Image information and resizing
    NUM_IMAGES = len(images)
    HEIGHT = 3024//4
    WIDTH = 4032//4
    CHANNELS = 3
    SHAPE = (HEIGHT, WIDTH, CHANNELS)
    
    with h5py.File('imagedata.h5', 'w') as hf: 

        for i,img in enumerate(tqdm(images)): 
            image = io.imread(img)
            image = resize(image, (WIDTH,HEIGHT),  anti_aliasing=True)
            data.append(image)
            np.savez("progressivesave", images=data[i])

        #data.to_hdf("imagedata.h5", "images",mode="w")
        #want to save a new image to h5 one at a time like the npz
            # imgs = hf.create_dataset(
            #     name='images',
            #     data=data,
            #     #shape=(HEIGHT, WIDTH, CHANNELS),
            #     #maxshape=(HEIGHT, WIDTH, CHANNELS),
            #     compression="gzip",
            #     compression_opts=9)
    hf.close()
    imgs = np.array(data)
    np.savez("dataimages",images=data)

if __name__== "__main__":
   main()