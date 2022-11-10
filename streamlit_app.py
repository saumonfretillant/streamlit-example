# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

genre = st.sidebar.radio(
    "Quel Texte Analyser ?",
    ('Avis dataset', 'Texte Libre'))
if genre == 'Avis dataset':
    st.write('You selected comedy.')
else:
    text= st.sidebar.text_input("Entrez un texte:")

categories_count = ['1', '2', '3']
chosen_count = st.selectbox(
    'Choisir le nombre de topic !',
    categories_count
)

if st.button("Detecter le sujet d'insatisfaction"):
    st.write('detecter le sujet')
number = st.number_input('Insert a number',min_value=1,max_value=15,step=1)
st.write('The current number is ', number)



