import streamlit as st
from PIL import Image

title = "Deep in the clouds."
sidebar_name = "Accueil"


def run():

    # TODO: choose between one of these GIFs
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")

    #st.image("https://thumbs.gfycat.com/ChubbyEnviousGrizzlybear-mobile.mp4")
    st.image(Image.open("assets/ScornfulWindingHoki-mobile.gif"))
    
    st.title(title)

    st.markdown("---")

    st.markdown(
        """
        
        Voici une démonstration de notre projet DataScientest avec [Streamlit](https://streamlit.io).
       
        """
    )
