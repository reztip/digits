import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Take a single line pandas dataframe row of length n^2, 
# return n x n numpy array

def reshape_image(row_number, dframe):
    data_row = dframe[row_number:(row_number + 1)].values[0]
    n = np.sqrt(data_row.size).astype(np.int)
    img = list()
    for i in range(n):
        row = np.array(data_row[i * n : (i + 1) * n])
        img.append(row)
    img = np.array(img)
    return img

def reshape_image_by_row(data_row):
    data_row = data_row.values[0]
    n = np.sqrt(data_row.size).astype(np.int)
    img = list()
    for i in range(n):
        row = np.array(data_row[i * n : (i + 1) * n])
        img.append(row)
    img = np.array(img)
    return img


def get_label(row_number, labels):
    return labels[row_number]

def print_image(img, label):
    plt.imshow(img)
    plt.title('Image of A Digit - Labeled as {0}'.format(label),\
            fontweight = 'bold', fontsize = 16)
    plt.show()
