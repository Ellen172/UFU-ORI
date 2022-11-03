from unidecode import unidecode
import re

entrada_vocabulario = open('/home/ellen/Documentos/UFU-ORI/TP01/ex02/vocabulario.txt', 'r')
vocabulario = entrada_vocabulario.read().split()

entrada_texto = open('/home/ellen/Documentos/UFU-ORI/TP01/ex02/texto.txt')
texto_lido = entrada_texto.read()
texto = re.sub(r'[^\w\s]','', unidecode(texto_lido)).lower().split()

freq = []
for termo in vocabulario: 
    if(termo in texto): 
        freq.append(1)
    else:
        freq.append(0)
print(freq)

entrada_vocabulario.close()
entrada_texto.close()