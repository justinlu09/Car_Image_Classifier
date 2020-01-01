import os
from skimage.io import imread
from skimage.transform import rescale
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.pipeline import Pipeline
import skimage
import pickle

# Data pre-processing

train_data_list = []
count = 0
train_dir = os.path.join('data', 'cars_train')
for category in os.listdir(train_dir):
    path = os.path.join(train_dir, category)
    for car_img in os.listdir(path):
        img_arr = imread(os.path.join(path, car_img))
        rescaled_img = rescale(img_arr, 0.5)
        train_data_list.append([rescaled_img, count])
    count += 1

print(train_data_list[0])













