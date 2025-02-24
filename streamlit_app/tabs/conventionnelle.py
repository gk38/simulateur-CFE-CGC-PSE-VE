# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:53:13 2025

@author: gabri
"""


import streamlit as st
#from utils import logo
st.logo("logo_cfe_gd.jpg",size="large")

def calcul_conv(salaire,anc,age,classif):
    
    if classif=="A,B,C,D,E":
        if (anc<=10):
            indemnite_leg=1/4*salaire/12*anc
        else:
            indemnite_leg=1/4*salaire/12*10+1/3*salaire/12*(anc-10)
        indemnite=indemnite_leg
    else:
        if anc<=7:
            indemnite_conv=1/5*salaire/12*anc
            indemnite_leg=1/4*salaire/12*anc
        elif anc<=10 and anc>7:
            indemnite_conv=1/5*salaire/12*7+3/5*salaire/12*(anc-7)
            indemnite_leg=1/4*salaire/12*anc
        
        else:
            indemnite_conv=1/5*salaire/12*7+3/5*salaire/12*(anc-7)
            indemnite_leg=1/4*salaire/12*10+1/3*salaire/12*(anc-10)
        
        indemnite=max(indemnite_conv,indemnite_leg)
        if age>=50 and age<55 and anc>=5:
            indemnite=indemnite*1.2
            if indemnite<3*salaire/12:
                indemnite=3*salaire/12
        elif age>=55 and age<60 and anc>=5:
            indemnite=indemnite*1.3
            if indemnite<6*salaire/12:
                indemnite=6*salaire/12
        elif age==61 and ret_tx_plein==False:
            indemnite=indemnite*0.95
            
        elif age==62 and ret_tx_plein==False:
            indemnite=indemnite*0.9
            
        elif age==63 and ret_tx_plein==False:
            indemnite=indemnite*0.8
            
        elif age>=64 and ret_tx_plein==False:
            indemnite=indemnite*0.6
        if indemnite>18*salaire/12:
            indemnite=18*salaire/12
            
    return indemnite


st.set_page_config(page_title="Calcul PSE", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)
st.write("##titre")
st.write("consigne")
st.title("calcul indemnites conventionnelles")
st.sidebar.write("toto")

col1,col2=st.columns(2)



salaire=col1.number_input("Salaire annuel", key="salaire")
anc=col1.number_input("ancienneté", key="anc")
age=col1.number_input("age", key="age")
classif=col1.selectbox("classification",["A,B,C,D,E","F,G,H"])
ret_tx_plein=col1.selectbox("déjà elligible à la retraite à taux plein",["non","oui"])


col2.metric("montant conventionnelle",calcul_conv(salaire,anc,age,classif))


#salaire=st.number_input("Salaire annuel", key="salaire")
#anc=st.number_input("ancienneté", key="anc")
#age=st.number_input("age", key="age")
#classif=st.selectbox("classification",["A,B,C,D,E","F,G,H"])
#ret_tx_plein=st.selectbox("déjà elligible à la retraite à taux plein",["non","oui"])


#st.metric("montant conventionnelle",calcul_conv(salaire,anc,age,classif))