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
path = "/home/ellen/Documentos/UFU-ORI/TP02/ex03/hinos"
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

# imprindo no arquivo resposta 

file_resposta = open("/home/ellen/Documentos/UFU-ORI/TP02/ex03/resposta.txt", "w")

file_resposta.write("\ta) Qual o tamanho do vocabulário da coleção?\n\n")

voc=1
file_resposta.write("termos: ")
for termo in termos_vocabulario: 
    file_resposta.write(termo + ",")
    voc += 1
file_resposta.write("\n\n" + "O vocabulario possui " + str(voc-1) + " termos\n")

file_resposta.write("\n\tb) Encontre o TF-IDF de cada um dos documentos da coleção.\n")

maior_tf_idf = 0
maior_termo = termos_vocabulario[0]
maior_doc = files[0]
i_doc = 0
for list in list_tf_idf: 
    i_termo = 0
    #print("doc = " + files[i_doc])
    file_resposta.write("\n" + str(files[i_doc]) + ":\n")
    for tf_idf in list : 
        #print(termos_vocabulario[i_termo] + " = " + str(tf_idf))
        file_resposta.write(termos_vocabulario[i_termo] + " = " + str(round(tf_idf, 3)) + " | ")
        if (tf_idf > maior_tf_idf):
            maior_tf_idf = tf_idf
            maior_termo = termos_vocabulario[i_termo]
            maior_doc = files[i_doc]
        i_termo+=1
    file_resposta.write("\n")
    i_doc +=1

file_resposta.write("\n\tc) Qual termo(s), em qual documento, possui o maior peso TF-IDF?\n")

file_resposta.write("\nO termo com maior TF-IDF é o '" + str(maior_termo) + "' no documento '" + str(maior_doc) + "' com o valor de " + str(maior_tf_idf))  