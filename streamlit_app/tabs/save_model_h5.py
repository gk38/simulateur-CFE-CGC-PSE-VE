# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 15:41:23 2021

@author: Julien
"""

import segmentation_models as sm
import tensorflow as tf
from tensorflow import reduce_sum
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization
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

###Model 1
BACKBONE1 = 'resnet34'


# define model
model1 = sm.Unet(BACKBONE1, encoder_weights='imagenet', classes=4, activation='sigmoid')



model1.compile(optimizer=tf.keras.optimizers.Adam(learning_rate = 0.0001),
              #loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              loss = dice_loss,
              metrics=[dsc,"accuracy"])

## Creation of the directory to save the weights

directory_model = 'C:/Users/Julien/Documents/DataScientest/Projet/Data_aug/Model1/'

## Loads of the weight from previous fit
model1.load_weights(directory_model)


model1.save(directory_model + 'saved_model1.h5')

new_model = tf.keras.models.load_model(directory_model + 'saved_model1.h5', 
                                       custom_objects={'dice_loss': dice_loss, 'dsc' : dsc})

# Check its architecture
new_model.summary()








