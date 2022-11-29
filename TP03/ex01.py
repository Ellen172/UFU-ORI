from unidecode import unidecode
import re
import numpy as np 

# FUNÇÕES:  

def calcular_freq(termo, list): 
	cont = 0
	for elem in list: 
		if elem == termo : 
			cont +=1
	return cont

def calcular_tf_idf(bag_of_words, freq_termo_colecao):
	tf_idf = []
	n=0
	for freq in bag_of_words: 
		if (freq_termo_colecao[n] > 0 and freq >0): 
			num = (1+np.log2(freq))*(np.log2(5/freq_termo_colecao[n]))
		elif (freq > 0): 
			num = (1+np.log2(freq))
		else: 
			num = 0
		n+=1
		tf_idf.append(num)
	return tf_idf

def printar_tf_idf(tf_idf, vocabulario):
	n=0
	for termo in vocabulario: 
		print("termmo: " + str(termo) + "\t" + " tf-idf: " + str(tf_idf[n]))
		n+=1


# LETRA A

d1 = "logan e ororo são x-men"
d2 = "stark, parker e logan já foram vingadores parker gostaria de ser novamente"
d3 = "ororo e stark não são guardiões e sim vingadores, groot e rocket são guardiões mas poderiam ser vingadores"
d4 = "eu sou groot logan todos somos groot o groot irá ajudar ororo e os x-men"
d5 = "rocket e groot formam uma boa dupla nos guardiões rocket é maluco mas adora o groot"

vocabulario = {"logan", "ororo", "stark", "parker", "groot", "rocket", "x-men", "vingadores", "guardioes"}

# lista de termos dos documentos

termos_d1 = re.sub(r'[^\w\s]','', unidecode(d1)).lower().split()
termos_d2 = re.sub(r'[^\w\s]','', unidecode(d2)).lower().split()
termos_d3 = re.sub(r'[^\w\s]','', unidecode(d3)).lower().split()
termos_d4 = re.sub(r'[^\w\s]','', unidecode(d4)).lower().split()
termos_d5 = re.sub(r'[^\w\s]','', unidecode(d5)).lower().split()

# bag of words para cada documento 

bow_d1 = []
bow_d2 = []
bow_d3 = []
bow_d4 = []
bow_d5 = []

for termo in vocabulario: 
	if termo in termos_d1: 
		bow_d1.append(1)
	else: 
		bow_d1.append(0)
	if termo in termos_d2: 
		bow_d2.append(1)
	else: 
		bow_d2.append(0)
	if termo in termos_d3: 
		bow_d3.append(1)
	else: 
		bow_d3.append(0)
	if termo in termos_d4: 
		bow_d4.append(1)
	else: 
		bow_d4.append(0)
	if termo in termos_d5: 
		bow_d5.append(1)
	else: 
		bow_d5.append(0)

# frequencia do termo na coleção

freq_termo_colecao = []
for termo in vocabulario: 
	cont = 0
	if termo in termos_d1: 
		cont +=1
	if termo in termos_d2: 
		cont +=1
	if termo in termos_d3: 
		cont +=1
	if termo in termos_d4: 
		cont +=1
	if termo in termos_d5: 
		cont +=1
	freq_termo_colecao.append(cont)	

# calcular td-idf

tf_idf_d1 = calcular_tf_idf(bow_d1, freq_termo_colecao)
tf_idf_d2 = calcular_tf_idf(bow_d2, freq_termo_colecao)
tf_idf_d3 = calcular_tf_idf(bow_d3, freq_termo_colecao)
tf_idf_d4 = calcular_tf_idf(bow_d4, freq_termo_colecao)
tf_idf_d5 = calcular_tf_idf(bow_d5, freq_termo_colecao)

# printar resultado final

#print("Valores TF-IDF para cada termo em cada documento: ")
#print("------ Documento 01 ------")
#printar_tf_idf(tf_idf_d1, vocabulario)
#print("------ Documento 02 ------")
#printar_tf_idf(tf_idf_d2, vocabulario)
#print("------ Documento 03 ------")
#printar_tf_idf(tf_idf_d3, vocabulario)
#print("------ Documento 04 ------")
#printar_tf_idf(tf_idf_d4, vocabulario)
#print("------ Documento 05 ------")
#printar_tf_idf(tf_idf_d5, vocabulario)


# LETRA B 

q = "logan ororo x-men"
termos_q = {'logan', 'ororo', 'x-men'}

# frequencia dos termos na consulta 
	
bow_q = []
for termo in vocabulario: 
	if termo in termos_q: 
		bow_q.append(calcular_freq(termo, termos_q))
	else : 
		bow_q.append(0)

# calcular tf-idf dos termos da consulta

tf_idf_q = calcular_tf_idf(bow_q, freq_termo_colecao)

# calcular normas dos documentos