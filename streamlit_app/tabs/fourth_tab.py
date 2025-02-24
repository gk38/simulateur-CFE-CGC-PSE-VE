import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import random
import os

title = "Présentation du modèle et résultats"
sidebar_name = "Présentation du modèle et résultats"


def run():

    st.title(title)
    
    st.markdown("---")
    
    st.markdown(
        """
        ### Modèle utilisé:
        Dans cette section, le modèle mis en oeuvre est un U-Net avec un backbone MobileNet.
        Bien entendu, pour améliorer nos performances, le transfer learning a été utilisé.
        La fonction de perte utilisée est la dice loss.
        En ce qui concerne l'optimiseur, il s'agit du Radam.
        
        Maintenant regardons ce que notre modèle prédit sur les images du dataset à l'aide du bouton ci-dessous.(appuyer plusieurs fois pour visualiser plusieurs exemples)
       
        """
        )

    if st.button('Charger les images et les masques'):
        ix=random.randint(101,132)
        chemin=str(ix)
        st.image(Image.open(os.path.join('assets\\images',chemin +'.png')),caption='Masques réels vs masques prédits',width = 900)
        

    


        
    
