import streamlit as st
import pandas as pd
import numpy as np
import import_image_NASA as iin
import predict_from_picture as pfp
import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as patches

title = "Détection de nuage personnalisée"
sidebar_name = "Détection de nuage personnalisée"




##Déclaration des constantes de la map monde
pix_p_deg = 5 #number of pixels per degree
lat_min = -80.0
lat_max = 65.0
long_min = -180.0
long_max = 180.0

## Constantes pour que les images collent au datset kaggle
lat_size = 14 ## Do not modify to be like the kaggle dataset
long_size = 21 ## Do not modify to be like the kaggle dataset 

## dates initiales
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1) ## init date is yesterday

##map monde avec valeur initiales
glob = iin.retrieve_image(yesterday, lat_min, lat_max, long_min, long_max, 
                          (lat_max-lat_min )*pix_p_deg,
                          (long_max-long_min )*pix_p_deg)

def run():


    st.title(title)
    
    st.markdown("---")

    st.markdown(
        """
        ### Détection de formations nuageuses à partir d'images satellite de la NASA
        
        Cet onglet permet à l'utilisateur de choisir une région et une date à partir de laquelle il est possible de prédire les formations nuageuses qui s'y trouvent.
        Les images satellites présentées sont issues du programme [Worldview](https://worldview.earthdata.nasa.gov/) de la NASA.
        """
    )
    
    #### Choix dans la date
    st.markdown(
        """
        #### Sélection de la date
        """
        )
    if 'date' not in st.session_state:
        st.session_state['date'] = yesterday
        
    if 'world' not in st.session_state:
        st.session_state['world'] = glob
        
    date = st.date_input("", 
                      value = yesterday,
                      min_value = datetime.date(2000, 3, 1),
                      max_value = today)
    
    st.session_state['date'] = date
    
   
    ### Initilization de la map monde
    st.session_state['world'] = iin.retrieve_image(st.session_state['date'], 
                                                   lat_min, lat_max, long_min, long_max, 
                      (lat_max-lat_min )*pix_p_deg,
                      (long_max-long_min )*pix_p_deg)

        
### Création de la zone de sélection avec curseur
    st.markdown(
        """
        #### Sélection des coordonnées
        """
        )
    
    if 'firstla' not in st.session_state:
        st.session_state['firstla'] = 0.00
    if 'firstlo' not in st.session_state:
        st.session_state['firstlo'] = 0.00

    
    st.slider('Latitude', lat_min, lat_max, None,0.01, key='firstla')
    latitude=st.session_state.firstla
    
    st.slider('Longitude', long_min, long_max, None,0.01, key='firstlo')
    longitude=st.session_state.firstlo
    

    


    # Create figure and axes
    fig, ax = plt.subplots()
    
    # Display the map
    ax.imshow(st.session_state['world'])
    
    # Create a Rectangle patch
    rect = patches.Rectangle(((longitude - long_min - long_size/2)*pix_p_deg,
                              (-latitude + lat_max - lat_size/2)*pix_p_deg),
                            
                             long_size*pix_p_deg, lat_size*pix_p_deg, linewidth=1, 
                             edgecolor='r', facecolor='none')
    
    # Add the patch to the Axes
    ax.add_patch(rect)
    plt.axis('off')

    st.pyplot(fig)
    

        
    ## initialisation de la zone
    if 'selected_area' not in st.session_state:
        st.session_state['selected_area'] = glob
    st.markdown(
        """
        #### Si la zone vous convient, cliquez sur le bouton ci-dessous pour identifier les formations nuageuses
        """
        )
    
    ## prédictions des formations nuageuses et affichage
    predict_button = st.button('Prédire Formations')

    if 'loaded_area' not in st.session_state:
        st.session_state['loaded_area'] = False  
    
    if predict_button or st.session_state['loaded_area']:
        st.session_state['loaded_area'] = True
        img_selected = iin.retrieve_image_like_kaggle(latitude, 
                                                      longitude, 
                                                      st.session_state.date)
        st.session_state['selected_area'] = img_selected
        
        fig_list, label_list = pfp.viz_predictions_large(st.session_state['selected_area'])
        
        if len(fig_list)>0:
            st.markdown(
            """
            Les Formations suivantes ont été détectées:
                
            """
            )

                    
            formation = st.radio('', label_list)
       
            j = label_list.index(formation)            
            st.pyplot(fig_list[j])
                
           
        else:
            st.markdown(
            """
            Aucune formation détectée dans la zone sélectionnée:
            """
            )   
            st.image(st.session_state['selected_area'])
            st.markdown(
            """
            Veuillez choisir des coordonnées ou une date différente.
            """
            )

        
    
    


  
