

from flask import Flask
app = Flask(__name__)


import numpy as np
import re
import nltk
from sklearn.datasets import load_files
nltk.download('stopwords')
import pickle
from nltk.corpus import stopwords

movie_data = load_files(r"C:\Users\Jessica\Desktop\TEXTOS")
X, y = movie_data.data, movie_data.target

#   PROCESAMIENTO PARA LIMPIAR EL TEXTO

documents = []

from nltk.stem import WordNetLemmatizer

from unicodedata import normalize

stemmer = WordNetLemmatizer()
import stanza

stanza.download('es')
nlp = stanza.Pipeline('es')

texto = ['palabras, Con         acénto','otras pruebas','esto lo hago pa Divertime','otrooos']

for sen in range(0, len(X)):
    # Remove all the special characters
    #document = re.sub(r'W', ' ', )

    # -> NFD y eliminar diacríticos
    document = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize("NFD", str(texto[sen])), 0, re.I
    )

    # remove all single characters
    document = re.sub(r's+[a-zA-Z]s+', ' ', document)

    # Remove single characters from the start
    document = re.sub(r'^[a-zA-Z]s+', ' ', document)

    # Substituting multiple spaces with single space
    document = re.sub(r's+', ' ', document, flags=re.I)

    # Removing prefixed 'b'
    document = re.sub(r'^bs+', '', document)

    # Converting to Lowercase
    document = document.lower()

    # Lemmatization
    #document = document.split()

    #document = [stemmer.lemmatize(word) for word in document]
    #document = " ".join(document)

    document = nlp(document)

    documents.append(document)


import json
documents2 =[]
json_extra = json.loads(str(documents))
print(json_extra)
json_biografia = json_extra[0][0]
print(json_biografia)


print(len(json_extra[0]))


for sen in range(0, len(json_extra)):
    doc = ''
    extra = json_extra[sen][0]
    for i in range(0, len(extra)):
        doc = doc + str(extra[i]['lemma']) + ' '
    documents2.append(doc)

print('salidaaaaaa')
print (documents2)


f = open(r'C:\Users\Jessica\Desktop\me-tienes-la-vida-piche.txt', 'w')
f.write(str(documents))
f.close()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

