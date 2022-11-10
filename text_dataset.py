
import pandas as pd
DATASET_FILE = "dataset.csv"
import pickle
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

def text_dataset(index):
    df = pd.read_csv(DATASET_FILE)
    return(df.text[index])

def vect():
    with (open("vectorizer", "rb")) as f:
        vectorizer = pickle.load(f)
    return vectorizer
