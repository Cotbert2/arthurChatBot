#chatbot with nlp and deep learning
import nltk
from nltk.translate.bleu_score import sentence_bleu
from model import NeuratNet


nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


lemmatizer = nltk.WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])

    tokens = nltk.word_tokenize(text)
    tokens = [token for token in tokens if token not in nltk.corpus.stopwords.words('english')]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens



reference = "The quick brown fox jumps over the lazy dog"
candidate = "The quick brown fox jumps over the lazy dog"
reference = preprocess_text(reference)
reference = [reference]
candidate = preprocess_text(candidate)

score = sentence_bleu(reference, candidate)
print(score)