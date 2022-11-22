import os
import re 
from unidecode import unidecode
import numpy

vocabulario_file = open("/home/ellen/Documentos/UFU-ORI/TP02/vocabulario.txt", 'r')
vocabulario = vocabulario_file.read()
termos_vocabulario = re.sub(r'[^\w\s]','', unidecode(vocabulario)).lower().split() 

list_termos_docs = []

path = "/home/ellen/Documentos/UFU-ORI/TP02/docs"
os.chdir(path)
for file in os.listdir(): 
    file_path = f"{path}/{file}"
    documento_file = open(file_path, 'r')
    documento = documento_file.read()
    termos_doc = re.sub(r'[^\w\s]','', unidecode(documento)).lower().split() 
    list_termos_docs.append(termos_doc)

list_bag_of_words = []
for termos_doc in list_termos_docs: 
    bag_of_words = []
    for termo in termos_vocabulario: 
        if (termo in termos_doc) : 
            bag_of_words.append(1)
        else : 
            bag_of_words.append(0)
    list_bag_of_words.append(bag_of_words)

for bag_of_words in list_bag_of_words: 
    for freq_termo in bag_of_words: 
        tf_df = (1 + numpy.log2(freq_termo) * numpy.log2(nro_documentos / freq_termo_colecao))

        # numpy.log2()