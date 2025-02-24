# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 11:10:17 2021

@author: Julien
"""
import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

#st.cache
def retrieve_image(date, min_lat, max_lat, min_long, max_long, pix_height, pix_width):

  url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&LAYERS=MODIS_Aqua_CorrectedReflectance_TrueColor&CRS=EPSG:4326&TIME={date}&WRAP=DAY&BBOX={min_lat},{min_long},{max_lat},{max_long}&FORMAT=image/jpeg&WIDTH={pixel_width}&HEIGHT={pixel_height}&AUTOSCALE=TRUE&ts=1636363623250'.format(
      date = date,
      pixel_width = int(pix_width),
      pixel_height = int(pix_height),
      min_lat = min_lat,
      min_long = min_long,
      max_lat = max_lat,
      max_long = max_long,

  )

  response = requests.get(url)
  img = Image.open(BytesIO(response.content))

  return img


#@st.cache
def retrieve_image_like_kaggle(center_box_lat, center_box_long, date):
    lat_size = 14 ## Do not modify to be like the kaggle dataset
    long_size = 21 ## Do not modify to be like the kaggle dataset 
       
    pixels_number_per_degree = 50
        
    img_kaggle = retrieve_image(date = date, min_lat = center_box_lat - lat_size/2, max_lat = center_box_lat + lat_size/2, 
                   min_long= center_box_long - long_size/2, max_long =center_box_long + long_size/2,
                   pix_height = pixels_number_per_degree*lat_size , pix_width = pixels_number_per_degree*long_size)
    return img_kaggle

if __name__ == "__main__":
    
    
    

    center_box_lat = 43
    center_box_long = 0
    date = '2020-09-23'
    pix_p_deg = 5
    img_test = retrieve_image_like_kaggle(center_box_lat, center_box_long, date)
    img_test = retrieve_image(date, -90, 90, -180, 180, 1000, 2000)
    
    glob = retrieve_image(date, -90.0, 90.0, -180.0, 180.0, 
                              180*pix_p_deg,
                              360*pix_p_deg)
    
    plt.imshow(glob)
