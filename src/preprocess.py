import pandas as pd
import re
import string
from sklearn.model_selection import train_test_split

def load_data(path):
    df = pd.read_csv(path, encoding='latin-1')
    df = df[['v1', 'v2']]
    df.columns = ['label', 'text']
    return df

def clean_text(text):
    text = str(text).lower()

    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[₹$€£]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text

def preprocess_data(df):
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})
    df['text'] = df['text'].apply(clean_text)
    return df

def split_data(df):
    X = df['text']
    y = df['label']
    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)