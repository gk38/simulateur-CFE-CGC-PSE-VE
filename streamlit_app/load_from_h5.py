# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:41:23 2021

@author: Julien
"""


import tensorflow as tf
from tensorflow import reduce_sum
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization


# Dice similarity coefficient loss, brought to you by: https://github.com/nabsabraham/focal-tversky-unet
def dsc(y_true, y_pred):
    smooth = 1.
    y_true_f = Flatten()(y_true)
    y_pred_f = Flatten()(y_pred)
    intersection = reduce_sum(y_true_f * y_pred_f)
    score = (2. * intersection + smooth) / (reduce_sum(y_true_f) + reduce_sum(y_pred_f) + smooth)
    return score

def dice_loss(y_true, y_pred):
    loss = 1 - dsc(y_true, y_pred)
    return loss


directory_model = ''



loaded_model = tf.keras.models.load_model(directory_model + 'streamlit_model.h5', 
                                           custom_objects={'dice_loss': dice_loss, 'dsc' : dsc})


# Check its architecture
if __name__ == "__main__":
    loaded_model.summary()








