import random
import json
import torch
from model import NeuratNetwork
from nlp_pipeline import bag_of_words, tokenize

#define use gpu isf its available or cpu instead
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#read the intents.json file
with open('./../DB/data.json', 'r') as json_data:
    intents = json.load(json_data)

#load the model wiht the prev trained data
FILE = "./../DB/data.pth"
data = torch.load(FILE)

#load model configuration

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuratNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()


#generate a function to response
def reponse(inputText):
    sentence = inputText
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.65:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    else:
        return "Sorry, currently my model is not trained to answer this question :("