from unidecode import unidecode
import re

# abrir arquivo no mesmo diretorio
texto = open('/home/ellen/Documentos/UFU-ORI/TP01/entrada1.txt', 'r') 

# ler arquivo (retorna em uma unica string)
entrada_lida = texto.read()

# modificar string lida
entrada_sem_acentos = unidecode(entrada_lida)
entrada_sem_pontuacao = re.sub(r'[^\w\s]','', entrada_sem_acentos)
entrada_minuscula = entrada_sem_pontuacao.lower()
lista_palavras = entrada_minuscula.split()

# criando vocabulario (sem repetições)
vocabulario = []
for palavra in lista_palavras: 
    if(palavra not in vocabulario):
        vocabulario.append(palavra)

# ordenando palavras
vocabulario.sort()

# criar arquivo de saida
saida = open('/home/ellen/Documentos/UFU-ORI/TP01/saida.txt', 'w')

# escrever no arquivo de saida
for vocabulo in vocabulario:
    saida.write(vocabulo + '\n')

# fechar arquivo
texto.close() 
saida.close()