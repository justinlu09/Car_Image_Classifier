import os
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.pipeline import Pipeline
import skimage
from skimage.io import imread

# Data pre-processing
train_dir = os.path.join('data', 'cars_train')
for category in os.listdir(train_dir):
    path = os.path.join(train_dir, category)
    for car_img in os.listdir(path):
        img_arr = imread(os.path.join(path, car_img), as_gray=True)











