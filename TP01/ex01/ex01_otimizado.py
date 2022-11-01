from unidecode import unidecode
import re

arquivo_entrada = open('/home/ellen/Documentos/UFU-ORI/TP01/entrada1.txt', 'r') 

texto = arquivo_entrada.read()
palavras = re.sub(r'[^\w\s]','', unidecode(texto)).lower().split()
vocabulario = sorted(set(palavras))

arquivo_saida = open('/home/ellen/Documentos/UFU-ORI/TP01/saida.txt', 'w')

for vocabulo in vocabulario:
    arquivo_saida.write(vocabulo + '\n')

# fechar arquivo
arquivo_entrada.close() 
arquivo_saida.close()