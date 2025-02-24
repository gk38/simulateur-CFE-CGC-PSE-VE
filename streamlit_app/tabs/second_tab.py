import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


title = "Presentation du projet"
sidebar_name = "Presentation du projet"


def run():

    st.title(title)
    
    st.markdown("---")

    st.markdown(
        """

        ## Contexte

La plupart des modèles pour prédire le climat se basent sur des échelles spatiales de nuages supérieures à 300 km. Certaines publications récentes montrent que la relation entre les propriétés des nuages ​​et les flux radiatifs n'est pas linéaire, la présence de variabilité des nuages ​​à des échelles plus petites (méso-échelle) crée des biais dans les flux radiatifs modélisés, et donc sur la qualité de la prédiction. Il est donc primordial de pouvoir prendre en compte les nuages de méso-échelle pour pouvoir mieux anticiper le climat et les catastrophes climatiques (de plus en plus nombreuses à l’échelle mondiale).
L’organisation des nuages de méso-échelle est visible par satellite, les spécialistes des instituts de météorologie sont capables de reconnaître des motifs mais il est très difficile de le faire de manière automatique.
C’est pourquoi le Max Planck Institute for Meteorology a lancé une étude pour évaluer la pertinence d’utiliser l’Intelligence Artificielle pour reconnaître ces motifs. Un challenge Kaggle a été lancé en 2019 pour trouver un modèle pour localiser et reconnaître 4 types de formations nuageuses (Flower, Fish, Gravel et Sugar).
 
        """
    )


    st.markdown(
       """

        ## Sommaire
        
        Cette démonstration Streamlit s'articule suivant plusieurs onglets:

        1. Accueil
        2. Présentation du projet
        3. Exploration des données
        4. Présentation du modèle et résultats
        5. Détection de nuages personnalisée à partir d'images satellite de la NASA

        """
    )