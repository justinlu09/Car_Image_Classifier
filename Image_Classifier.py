import os
from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt


''' Baseline Model '''


def create_training_data(resize_factor):    # Preparing training data
    train_data_list = []
    idx = 0
    train_dir = os.path.join('data', 'cars_train')
    for category in os.listdir(train_dir):
        path = os.path.join(train_dir, category)
        for car_img in os.listdir(path):
            try:
                img_arr = imread(os.path.join(path, car_img))
                resized_img = resize(img_arr, (img_arr.shape[0]//resize_factor, img_arr.shape[1]//resize_factor))
                train_data_list.append((resized_img, idx))
            except Exception as e:
                pass
        idx += 1
    return train_data_list


SIZE = 4
train_data = create_training_data(SIZE)














