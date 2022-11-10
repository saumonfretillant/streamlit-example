# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

genre = st.sidebar.radio('Quel Texte Analyser ?',('Avis dataset', 'Texte Libre'))
if genre == 'Avis dataset':
    number = st.sidebar.number_input('Choisir le numéro de l\'index',min_value=1,max_value=10000,step=1)
    if st.button('Prédire un avis via le numéro d\'index'):
        st.write(number)
    if st.button('Prédire un avis aléatoire'):
        st.write('RANDOM')
else:
    text= st.sidebar.text_input("Entrez un nouvel avis:")

number = st.number_input('Choisir le nombre de topics',min_value=1,max_value=15,step=1)
st.write('The current number is ', number)

if st.button("Detecter le sujet d'insatisfaction"):
    st.write('detecter le sujet')




