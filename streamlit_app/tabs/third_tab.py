import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import random
import os
#from bokeh.plotting import figure, show, output_file
import plotly.graph_objects as go
import plotly.express as px

title = "Exploration des données"
sidebar_name = "Exploration des données"







def run():

    st.title(title)
    
    st.markdown("---")
    
    st.markdown(
        """
        ### Dataset
        
        Notre dataset est constitué de 5546 images, nous fournissant 11836 labels (type de structures + localisation).
        """
    )


    st.markdown(
        """
        ### Présentation des images du dataset et des formations nuageuses
        
        Appuyer sur ce bouton pour charger de manière aléatoire les masques associés à 1 image (appuyer plusieurs fois pour visualiser plusieurs exemples) 
        
        
        
        
        
        """
    )


    
    if st.button('Charger les images et les masques'):
        ix=random.randint(1,32)
        chemin=str(ix)
        st.image(Image.open(os.path.join('assets\\images',chemin +'.png')),caption='Image du dataset et masques associés',width = 900)

        
       


    st.markdown(
        """
    ### Quelques statistiques
            
    ##### Répartition des formations dans le dataset
            
    
    
        """
        )
    
    
    
    
    
    
    
    formations=['Fish', 'Flower',
          'Gravel', 'Sugar']

    values = [23.5, 19.98,24.83,31.69]
   
    fig = go.Figure(
    go.Pie(
    labels = formations,
    values = values,
    hole = 0.2,
    hoverinfo = "label+percent",
    textinfo = "value"
    ))
   
    #st.header("")
    
    
    
    
    fig.update_layout(
    title={
        'text': "Répartition des types de formations dans le dataset",
        'y':0.08,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'bottom'})

    st.plotly_chart(fig)





    #$st.image(Image.open("assets/camembert.png"), caption='Nombre de formations dans le dataset',width = 400)
    
    st.markdown(
        """
        
        
        On observe que la répartition entre "Flower", "Fish", "Gravel" et "Sugar" est assez équilibrée...
        
        
        
        
        """
    )
    
    
    
    dict = {'Nombre de formations par image': [1,2,3,4],
            "Nombre d'images": [1348,2372,1560,266]}

    df = pd.DataFrame(dict)
    
    
    fig = px.bar(        
        df,
        x = "Nombre de formations par image",
        y = "Nombre d'images",
        #title = "Bar Graph",
        width = 500,height=400
    )
    
    
    
    col1, col2, col3 = st.columns([1,6,1])

    with col1:
        st.write("")

    with col2:
        
        st.plotly_chart(fig)

    with col3:
        st.write("")
    
    #st.image(Image.open("assets/barchart.png"), caption='Nombre de formations par image',width = 400)
    
    

    st.markdown(
        """
    
    
    
        On observe que la plupart des images contiennent 2 formations à la fois et peu d'entre elles en contiennent 4...
    
    
        """
        )