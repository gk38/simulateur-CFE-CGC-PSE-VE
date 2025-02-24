# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 10:24:34 2021

@author: Julien
"""

import tensorflow as tf
import load_from_h5 as lfh5

import os
os.environ["SM_FRAMEWORK"] = "tf.keras" #before the import

import segmentation_models as sm
import numpy as np
import matplotlib.pyplot as plt
import import_image_NASA as iin
import datetime

backbone = 'mobilenet'



IMG_HEIGHT = 320
IMG_WIDTH = 480


def format_image_NASA(img, backbone, resize=(IMG_HEIGHT,IMG_WIDTH)):

  input_image = np.array(img)
  #input_image = tf.image.decode_jpeg(img, channels=3)
  input_image = tf.cast(input_image, tf.float32)
 
  input_image = tf.image.resize(input_image, resize)
  input_image = sm.get_preprocessing(backbone)(input_image)
  
  return input_image

def viz_cloud_img_mask(img, masks, label):
    img = tf.keras.preprocessing.image.array_to_img(img)
    fig, ax = plt.subplots(nrows=1, ncols=4, sharey=True, figsize=(20,10))
    cmaps = ["Reds", "Blues", "Greens", "Purples"]
        
    for i in range(4):    
        ax[i].imshow(img)
        ax[i].imshow(masks[:,:,i], alpha=0.3, cmap=cmaps[i])
        ax[i].set_title(label + ' Formation ' + str(i))

    return fig

def viz_cloud_img_mask_large(img, masks, label, threshold = 0.5):
    img = tf.keras.preprocessing.image.array_to_img(img)
    fig, ax = plt.subplots(nrows=1, ncols=4, sharey=True, figsize=(20,10))
    cmaps = ["Reds", "Blues", "Greens", "Purples"]
    fig_list = []    
    for i in range(4):    
        ax[i].imshow(img)
        ax[i].imshow(masks[:,:,i], alpha=0.3, cmap=cmaps[i])
        ax[i].set_title(label + ' Formation ' + str(i))

    return fig


def viz_predictions(img):
    formatted_image = format_image_NASA(img, backbone)
    formatted_image = tf.expand_dims(formatted_image, 0)
    
    pred = lfh5.loaded_model.predict(formatted_image)
    
    
    fig = viz_cloud_img_mask(formatted_image[0], pred[0], '')
    return fig


def viz_predictions_large(img):
    img_shape = np.array(img).shape[0:2]
    formatted_image = format_image_NASA(img, backbone)
    formatted_image = tf.expand_dims(formatted_image, 0)
    
    pred = lfh5.loaded_model.predict(formatted_image)
    
    pred = tf.image.resize(pred, img_shape)
    
    pred = np.array(pred)[0]
    
    cmaps = ["Reds", "Blues", "Greens", "Purples"]
    labels = ['Fish', 'Flower', 'Gravel', 'Sugar']
    fig_list = [] 
    label_list = []
    for i in range(4): 
        fig = plt.figure()
        plt.imshow(img)
        plt.imshow(pred[:,:,i], alpha=0.3, cmap=cmaps[i])
        plt.axis('off')
        if pred[:,:,i].max() > 0.5:
            fig_list.append(fig)
            label_list.append(labels[i])
        
    
    
    return fig_list, label_list


if __name__ == "__main__":
    date = datetime.date(2021,6,6)
    center_box_lat = 0
    center_box_long = 0
    img_test = iin.retrieve_image_like_kaggle(center_box_lat, center_box_long, date)
    fig_list, label_list = viz_predictions_large(img_test)


