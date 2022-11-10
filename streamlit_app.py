# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import altair as alt
import pandas as pd
import streamlit as st
import random as rd
from text_dataset import text_dataset

genre = st.sidebar.radio('Quel Texte Analyser ?',('Avis dataset', 'Texte Libre'))
if genre == 'Avis dataset':
    number = st.sidebar.number_input('Choisir le numéro de l\'index',min_value=1,max_value=10000,step=1)
    if st.sidebar.button('Prédire un avis via le numéro d\'index'):
        st.sidebar.write(text_dataset(number-1))
    if st.sidebar.button('Prédire un avis aléatoire'):
        random = rd.randint(0,9999)
        st.sidebar.write(text_dataset(random))
else:
    text= st.sidebar.text_input("Entrez un nouvel avis:")

number = st.number_input('Choisir le nombre de topics',min_value=1,max_value=15,step=1)
st.write('The current number is ', number)

if st.button("Detecter le sujet d'insatisfaction"):
    st.write()




