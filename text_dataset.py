
import pandas as pd
DATASET_FILE = "dataset.csv"
import pickle
import sklearn

def text_dataset(index):
    df = pd.read_csv(DATASET_FILE)
    return(df.text[index])

def load(file):
    with (open(file, "rb")) as f:
        while True:
            try:
                model = pickle.load(f)
            except EOFError:
                break
