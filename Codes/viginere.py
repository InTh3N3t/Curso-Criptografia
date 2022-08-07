#!/usr/bin/env python
#Biblioteca sys: Requisito para a passagem de parâmetros na linha de comando.
import sys
#Biblioteca string: Importando a string lowercase, que contém todas as letras.
minúsculas do alfabeto, e dando a ela o nome de lc.
from string import lowercase as lc
#Usando o argumento passado na linha de comando (sys.argv[1]) como um nome de arquivo. Read() transforma o conteúdo do arquivo em string e lower() passa todas as letras para minúsculas.
file = open(sys.argv[1],'r').read().lower()
#Usa o Segundo argumento passado como a chave.
key = sys.argv[2].lower()
#Usa o terceiro argumento passado como modo de operação: enc ou dec.
mode = sys.argv[3]
result = ''
#Armazena a posição de cada letra da palavra-secreta.
keyidx = 0
#Executa uma vez para cada caractere do texto.
for lt in file:
#Se o caractere for uma letra.
if lt in lc:
#Armazena a posição dessa letra no alfabeto.
idx = lc.find(lt)
#Se o modo for de encriptação.
if mode == 'enc':
#Soma a posição da letra com a posição da letra da palavra-secreta.
idx += lc.find(key[keyidx%len(key)])
#Se o modo for decriptografiaelif mode == 'dec':
#Subtrai a posição da letra da palavra-secreta da posição da letra do texto.
idx -= lc.find(key[keyidx%len(key)])
#Concatena o resultado na variável result.
result += lc[idx%26]
keyidx += 1
#Caso o caractere não seja uma letra.
else:
#Concatena o caractere na variável result.
result += lt
print result,