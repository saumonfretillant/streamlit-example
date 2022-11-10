
import pandas as pd
DATASET_FILE = "dataset.csv"

def text_dataset(index):
    df = pd.read_csv(DATASET_FILE)
    return(df.text[index])
