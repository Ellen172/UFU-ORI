from unidecode import unidecode
import re

entrada_vocabulario = open('/home/ellen/Documentos/UFU-ORI/TP01/ex02/vocabulario.txt', 'r')
vocabulario = entrada_vocabulario.read().split()
print('vocabulario: ')
print(vocabulario)

entrada_texto = open('/home/ellen/Documentos/UFU-ORI/TP01/ex02/texto.txt')
texto_lido = entrada_texto.read()
texto = re.sub(r'[^\w\s]','', unidecode(texto_lido)).lower().split()
print('texto: ')
print(texto)

entrada_vocabulario.close()
entrada_texto.close()