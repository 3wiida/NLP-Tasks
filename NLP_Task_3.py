from nltk import ngrams
import nltk
import pandas as pd

dataset_path = "Dataset/emotion_dataset.csv"

def read_dataset(path):
    return pd.read_csv(path,dtype=str)

def get_ngrams(text, n):
    tokens = nltk.word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

def process():
    n = int(input("Enter number of N: "))
    data_frame = read_dataset(dataset_path)
    for _, row in data_frame.iterrows():
        n_grams = get_ngrams(row["text"], n)
        print(f"Text: {row['text']}")
        print(f"{n}-grams: {n_grams}\n")

process()