"""
This Python script sorts the car images into their respective categories
"""

import pandas as pd
import shutil

anno = pd.read_csv('train_annotations.csv')
anno['fname'] = anno['fname'].str[:-1]

classes = pd.read_csv('class_annotations.csv')
classes['Class'] = classes['Class'].str[:-1]
classes['Class'] = classes['Class'].str.replace('/', '')

anno_w_class = anno.copy()
anno_w_class['class'] = anno_w_class['class'].apply(lambda x: classes.iloc[x-1].values[0])
result_df = anno_w_class[['class', 'fname']]
class_df = result_df.set_index('class')

img_list = class_df['fname'].tolist()
for image in img_list:
    shutil.move('cars_train\\' + image, 'classes_folder\\' + class_df.loc[class_df['fname'] == image].index[0])
