import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler

def bigram_split(text):
    text = '$' + text + '$'
    return [text[i:i+2] for i in range(len(text)-1)]

def bigram_list(text_list):
    bigrams = []
    for text in text_list:
        for level in text.split('.'):
            bigrams += bigram_split(level)
            
    return bigrams

def bigram_freq2(bigrams_list):
    bigram_freq = {}
    for bigram in bigrams_list:
        if bigram in bigram_freq:
            bigram_freq[bigram] += 1
        else:
            bigram_freq[bigram] = 1
    for bigram in bigram_freq:
        bigram_freq[bigram] /= len(bigrams_list)
    return bigram_freq

        
def bigram_freq(bigrams_list):
    bigram_freq = {}
    for bigram in bigrams_list:
        if bigram in bigram_freq:
            bigram_freq[bigram] += 1
        else:
            bigram_freq[bigram] = 1
    return bigram_freq

def rank_bigrams_freq(bigram_freq):
    sorted_bigrams = sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True)
    
    ranked_bigrams = {bg: freq for i, (bg, freq) in enumerate(sorted_bigrams)}
    
    return ranked_bigrams

