import os
import re 
from unidecode import unidecode
import numpy

def contarFreq(termo, list):
    cont = 0
    for elem in list: 
        if elem == termo : 
            cont +=1 
    return cont

# definir termos dos documentos através de arquivos em pasta
termos_vocabulario = []
list_termos_docs = []
nro_documentos = 0
files = []
path = "/home/ellen/Documentos/UFU-ORI/TP02/docs"
os.chdir(path)
for file in os.listdir(): 
    # inserir na lista de documentos
    files.append(file) 
    # ler documento
    file_path = f"{path}/{file}"
    documento_file = open(file_path, 'r')
    documento = documento_file.read()
    documento_file.close()
    # definir termos do documento
    termos_doc = re.sub(r'[^\w\s]','', unidecode(documento)).lower().split() 
    # inserir no vocabulario 
    for termo in termos_doc: 
        if termo not in termos_vocabulario: 
            termos_vocabulario.append(termo)
    # inserir na lista de termos de documentos
    list_termos_docs.append(termos_doc)
    nro_documentos+=1


# criar bag of words dos documentos
list_bag_of_words = []
for termos_doc in list_termos_docs: 
    bag_of_words = []
    for termo in termos_vocabulario: 
        if (termo in termos_doc) : 
            bag_of_words.append(contarFreq(termo, termos_doc))
        else : 
            bag_of_words.append(0)
    list_bag_of_words.append(bag_of_words)

# definir freq dos termos na coleção
freq_termo_colecao = []
for termo_voc in termos_vocabulario: 
    num=0
    for termos_doc in list_termos_docs: 
        if(termo_voc in termos_doc): 
            num+=1
    freq_termo_colecao.append(num)

# definir tf-idf dos documentos
list_tf_idf = []
j=0
for bag_of_words in list_bag_of_words: 
    tf_idf = []
    i=0
    for freq_termo in bag_of_words: 
        if(freq_termo == 0): 
            tf_idf_termo = 0
        elif(freq_termo_colecao[i] == 0): 
            tf_idf_termo = 1 + numpy.log2(freq_termo)    
        else : 
            tf = 1 + numpy.log2(freq_termo)
            #print("freq_termo: " + str(freq_termo))
            idf = numpy.log2(nro_documentos / freq_termo_colecao[i])
            tf_idf_termo = (1 + numpy.log2(freq_termo)) * (numpy.log2(nro_documentos / freq_termo_colecao[i]))
        i+=1
        tf_idf.append(tf_idf_termo)
    list_tf_idf.append(tf_idf)
    j+=1

# imprimindo no console
k=0
for list in list_tf_idf: 
    print(files[k] + ": ")
    print(list)
    k+=1
