# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import altair as alt
import pandas as pd
import streamlit as st
import random as rd
from fonctions import fonction_prediction

import pandas as pd
DATASET_FILE = "dataset.csv"
import pickle
from PIL import Image

def text_dataset(index):
    df = pd.read_csv(DATASET_FILE)
    return(df.text[index])

def vect():
    with (open("vectorizer", "rb")) as f:
        vectorizer = pickle.load(f)
    return vectorizer

def model():
    with (open("model", "rb")) as f:
        model = pickle.load(f)
    return model

st.title("Analyseur de reviews")

image = Image.open('schema.jpg')
st.image(image)


genre = st.sidebar.radio('Quel texte analyser ?',('Avis du dataset', 'Nouvel avis'))
if genre == 'Avis du dataset':
    index = st.sidebar.radio('Quelle index voulez-vous choisir ?',('Choisir un index', 'Index aléatoire'))
    if index == 'Choisir un index':
        number = st.sidebar.number_input('Choisir le numéro de l\'index',min_value=1,max_value=10000,step=1)
        text = text_dataset(number-1)
    else:
        random = rd.randint(0,9999)
        text = text_dataset(random)
else:
    text = st.sidebar.text_input("Entrez un nouvel avis:")

number = st.number_input('Choisir le nombre de topics',min_value=1,max_value=15,step=1)
model = model()
vectorizer = vect()

if st.button("Detecter le sujet d'insatisfaction"):
    st.write('L\'avis choisi : ')
    st.write(text)
    st.write('')
    polarity, topics = fonction_prediction(model,vectorizer,number,text)
    for topic in topics:
        topic = '*'+topic+'*'
    if genre == 'Avis du dataset':
        st.write("les topics de l'avis sont : ")
        for topic in topics:
            st.write('-',topic)
    else:
        if polarity>0:
            st.write("polarité du nouvel avis : ",polarity,'(commentaire positif)')
        else:
            st.write("polarité du nouvel avis : ",polarity,'(commentaire négatif)')
        st.write("les topics de l'avis sont : ")
        for topic in topics:
            st.write('-',topic)
st.write('*ARNAUD Simon*')
