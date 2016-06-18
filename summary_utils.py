import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from digit_viewer import *
from sklearn.metrics import accuracy_score

def average_of_classes(full_dframe):
    grouped = full_dframe.groupby('label').aggregate(np.mean).\
            apply(np.round)
    return grouped


def average_of_class( grouped, labelnum):
    return grouped[labelnum : labelnum + 1]

def avg_img(full_dframe, labelnum):
    grouped = average_of_classes(full_dframe)
    avg_of_class = average_of_class(grouped, labelnum)
    return reshape_image_by_row(avg_of_class)

def score_classifier(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    print('-' * 30)
    print("The score on the data set is {:3.1f}%".\
     format(acc *  100)) 
    print('-' * 30)
    return acc















