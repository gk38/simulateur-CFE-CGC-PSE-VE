# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:54:23 2021

@author: Julien
"""

import tensorflow as tf


import tensorflow as tf
from tensorflow import reduce_sum
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
import segmentation_models as sm
sm.set_framework('tf.keras')


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


###Model 3
BACKBONE3 = 'mobilenet'


# define model
model3 = sm.Unet(BACKBONE3, encoder_weights='imagenet', classes=4, activation='sigmoid')

directory_model = r'C:\Users\Julien\Documents\DataScientest\Projet\Saved_models\Streamlit_model\\'

model3.load_weights(directory_model)

model3.save(directory_model + 'streamlit_model.h5')


loaded_model = tf.keras.models.load_model(directory_model + 'streamlit_model.h5', 
                                        custom_objects={'dice_loss': dice_loss, 'dsc' : dsc})

# Check its architecture
if __name__ == "__main__":
    loaded_model.summary()
