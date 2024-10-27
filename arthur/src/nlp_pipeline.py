import nltk
import numpy as np

def tokenize(text): #converts the text into tokens
    return nltk.word_tokenize(text)

def stem(word):#converts the word into its root form
    stemmer = nltk.PorterStemmer()
    return stemmer.stem(word)

def lemmatize(word): #converts the word into its base form
    lemmatizer = nltk.WordNetLemmatizer()
    return lemmatizer.lemmatize(word)

def bag_of_words(tokenized_words, all_words): #returns a list of 0s and 1s for the words in the sentence
    tokenized_words = [stem(w) for w in tokenized_words]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_words:
            bag[idx] = 1.0
    return bag

def stem_sentence(sentence): #converts the sentence into its root form
    stemmer = nltk.PorterStemmer()
    return ' '.join([stemmer.stem(word) for word in sentence])