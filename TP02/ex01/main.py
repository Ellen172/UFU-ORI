import os 
from unidecode import unidecode
import re

# lendo documentos 

path = "/home/ellen/Documentos/UFU-ORI/TP02/docs"
os.chdir(path) 

termosDocs = []
vocabulario = []
for file in os.listdir(): # para cada arquivo no diretorio especificado
    file_path = f"{path}/{file}"
    entrada = open(file_path, 'r') # abre arquivo
    doc = entrada.read(); # lê arquivo

    termosDoc = re.sub(r'[^\w\s]','', unidecode(doc)).lower().split() # pega cada palavra do arquivo, sem acentos ou pontuação, e transforma em minuscula
    termosDocs.append(termosDoc) # armazena a lista com as termosDoc de cada documento em uma lista
    
    for palavra in termosDoc: 
        if(palavra not in vocabulario): 
            vocabulario.append(palavra)

# salvando vocabulario em arquivo texto 

file_voc = open("/home/ellen/Documentos/UFU-ORI/TP02/vocabulario.txt", "w")
for termo in vocabulario: 
    file_voc.write(termo + "\n")

# bag of words

lista = []
for termosDoc in termosDocs: 
    bagOfWords = []
    for palavra in vocabulario: 
        if(palavra in termosDoc): 
            bagOfWords.append(1)
        else: 
            bagOfWords.append(0)
    lista.append(bagOfWords)

cont = 1
for bagOfWords in lista: 
    print("doc " + str(cont) + ": " + str(bagOfWords))
    cont+=1
