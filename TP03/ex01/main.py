import os
import re 
from unidecode import unidecode
import numpy

def contarFreq(termo, list):
    # retorna um numero inteiro igual a qtd de vezes que o termo aparece na list
    cont = 0
    for elem in list: 
        if elem == termo : 
            cont +=1 
    return cont

def definirTermosDoc(doc): 
    return re.sub(r'[^\w\s]','', unidecode(doc)).lower().split() 

def LerTermosDocAddress(doc_address):
    # definir termos do vocabulario dado
    file = open(doc_address, 'r')
    doc = file.read()
    termos = definirTermosDoc(doc)
    file.close()
    return termos

def calculaFreqTermoNoDoc(list_termos): 
    # dado uma lista de termos, calcula a frequencia de cada um (palavra-chave) no proprio documento
    list_freq = []
    for termo in list_termos: 
        if termo in termos_voc: 
            freq = contarFreq(termo, list_termos)
            list_freq.append(freq)
    return list_freq

def calculaFreqTermoNaColecao(list_termos):
    # dado uma lista de termos, calcula a freq de cada um na coleção de documentos
    freq_termo_colecao = []
    for termo in list_termos: 
        num=0
        for termos_doc in list_termos_docs: 
            if(termo in termos_doc): 
                num+=1
        freq_termo_colecao.append(num)   
    return freq_termo_colecao

def calculaVetor(freq_termo_doc, freq_termo_colecao): 
    # freq_termo_doc : lista com a frequencia de cada termo no proprio documento 
    # freq_termo_colecao : lista com a frequencia de cada termo do documento na coleção inteira 
    vetor = []
    i=0
    for freq in freq_termo_doc: 
        if (freq == 0) : 
            num_vet = 0
        elif (freq_termo_colecao[i] == 0) : 
            num_vet = 1 + numpy.log2(freq)    
        else : 
            num_vet = (1 + numpy.log2(freq)) * (numpy.log2(nro_docs / freq_termo_colecao[i]))
        vetor.append(num_vet)
        i+=1
    return vetor;



# PARAMETROS DE ENTRADA

voc_address = "/home/ellen/Documentos/UFU-ORI/TP03/ex01/vocabulario.txt"
#voc_address = input("Escreva o endereço do vocabulario: ")
path = "/home/ellen/Documentos/UFU-ORI/TP03/ex01/docs"
#path = input("Escreva o endereço do diretório que contém os documentos: ")
os.chdir(path) # defini path
q_address = input("Escreva a consulta: ")

# DEFINIR TERMOS 

termos_voc = LerTermosDocAddress(voc_address) # definir termos do vocabulario dado seu endereço
termos_q = definirTermosDoc(q_address) # definir termos da consulta 

# definir termos dos documentos através de arquivos em pasta
list_termos_docs = []
nro_docs = 0
docs_name = []
for file in os.listdir(): 
    # inserir na lista de documentos
    docs_name.append(file) 
    # ler documento e definir termos
    file_path = f"{path}/{file}"
    termos_doc = LerTermosDocAddress(file_path)
    # inserir na lista de termos de documentos
    list_termos_docs.append(termos_doc)
    nro_docs+=1


# DEFINIR FREQUENCIA 

# consulta
freq_termo_consulta = calculaFreqTermoNoDoc(termos_q) # definir freq dos termos da consulta na consulta (termos não podem estar repetidos)
freq_termo_consulta_colecao = calculaFreqTermoNaColecao(termos_q) # definir freq dos termos da consulta na coleção

vet_q = calculaVetor(freq_termo_consulta, freq_termo_consulta_colecao) # calcular vetor consulta

#definir frequencia dos termos dos documentos no proprio documento
list_freq_termos_doc = []
for termos_doc in list_termos_docs: 
    freq_termos_doc = calculaFreqTermoNoDoc(termos_doc)
    list_freq_termos_doc.append(freq_termos_doc)

freq_termo_doc_colecao = calculaFreqTermoNaColecao(termos_voc) # definir freq dos termos dos documentos na coleção

# definir vetor documento para cada documento
list_vet_doc = []
for freq_termo_doc in list_freq_termos_doc: 
    vet_doc = calculaVetor(freq_termo_doc, freq_termo_doc_colecao)
    list_vet_doc.append(vet_doc)

# calcular grau de similaridade


