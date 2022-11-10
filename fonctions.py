import numpy as np
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import contractions
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

tokenizer = RegexpTokenizer(r'\w+')
def tokenize_text(text):
    text_processed = " ".join(tokenizer.tokenize(text))
    return text_processed

import en_core_web_sm
nlp = en_core_web_sm.load(disable=['parser', 'tagger', 'ner'])

lemmatizer = WordNetLemmatizer()

def lemmatize_text(text):
    
    tokens_tagged = nltk.pos_tag(nltk.word_tokenize(text))
    lemmatized_text_list = list()
    
    for word, tag in tokens_tagged:
        if tag.startswith('J'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'a')) # Lemmatise adjectives. Not doing anything since we remove all adjective
        elif tag.startswith('V'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'v')) # Lemmatise verbs
        elif tag.startswith('N'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'n')) # Lemmatise nouns
        elif tag.startswith('R'):
            lemmatized_text_list.append(lemmatizer.lemmatize(word,'r')) # Lemmatise adverbs
        else:
            lemmatized_text_list.append(lemmatizer.lemmatize(word)) # If no tags has been found, perform a non specific lemmatisation
    
    return " ".join(lemmatized_text_list)

def normalize_text(text):
    return " ".join([word.lower() for word in text.split()])

def contraction_text(text):
    return contractions.fix(text)

negative_words = ['not', 'no', 'never', 'nor', 'hardly', 'barely']
negative_prefix = "NOT_"

def get_negative_token(text):
    tokens = text.split()
    negative_idx = [i+1 for i in range(len(tokens)-1) if tokens[i] in negative_words]
    for idx in negative_idx:
        if idx < len(tokens):
            tokens[idx]= negative_prefix + tokens[idx]
    
    tokens = [token for i,token in enumerate(tokens) if i+1 not in negative_idx]
    
    return " ".join(tokens)

from spacy.lang.en.stop_words import STOP_WORDS

def remove_stopwords(text):
    english_stopwords = stopwords.words("english") + list(STOP_WORDS) + ["tell", "restaurant"]
    
    return " ".join([word for word in text.split() if word not in english_stopwords])

def preprocess_text(text):
    
    # Tokenize review
    text = tokenize_text(text)
    
    # Lemmatize review
    text = lemmatize_text(text)
    
    # Normalize review
    text = normalize_text(text)
    
    # Remove contractions
    text = contraction_text(text)

    # Get negative tokens
    text = get_negative_token(text)
    
    # Remove stopwords
    text = remove_stopwords(text)
    
    return text

from textblob import TextBlob
import pandas as pd

def fonction_prediction(model, vectorizer, n_topics, text):
  topic_list = ['mauvais accueil','pas bon gout','mauvaise pizza','livraison retardée','rapport qualité/prix mauvais','mauvais service','mauvais burger','trop d\'attente','mauvais poulet','mauvaise ambiance au bar','mauvaise 2eme visite','manager rude et arrogant','mauvais sandwich','mauvais sushi','mauvaise experience d\'habitue']
  blob = TextBlob(text)
  polarity = blob.sentiment.polarity
  text = preprocess_text(text)
  text = [text]
  X = vectorizer.transform(text)
  doc_topic = model.transform(X)
  index=[]
  argsort = np.argsort(doc_topic, axis = 1 )
  for i in range(n_topics):
    index.append(argsort[0][len(argsort[0])-(i+1)])
  topics=[]
  for ind in index:
    topics.append(topic_list[ind])
  return polarity,topics
