
import asyncio
import numpy as np
import re
import nltk
from sklearn.datasets import load_files

from mlkit.app.command import Command
nltk.download('stopwords')
from unicodedata import normalize
import stanza
stanza.download('es')
from nltk.corpus import stopwords



class UseCaseGetCleanText(Command):
    print('NIVEL CASO DE USO')
    #   PROCESAMIENTO PARA LIMPIAR EL TEXTO

    def __init__(self):
        Command.__init__(self)

    async def execute():
        documents = []
        nlp = stanza.Pipeline('es')

        texto = ['palabras, Con         acénto','otras pruebas','Esto lo hago para Divertime','otrooos','otra cosa   es para ver']

        for sen in range(0, len(texto)):

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



        print(len(json_extra))


        for sen in range(0, len(json_extra)):
            doc = ''
            extra = json_extra[sen][0]
            for i in range(0, len(extra)):
                if i == len(extra)- 1 :
                    doc = doc + str(extra[i]['lemma'])
                else:
                    doc = doc + str(extra[i]['lemma']) + ' '
            documents2.append(doc)

        print('salidaaaaaa')
        print (documents2)


        f = open(r'C:\Users\Jessica\Desktop\me-tienes-la-vida-piche.txt', 'w')
        f.write(str(documents))
        f.close()