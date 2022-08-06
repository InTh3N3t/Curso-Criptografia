#!/usr/bin/env python
#Biblioteca sys: Requisito para a passagem de parâmetros na linha de comando
import sys
#Biblioteca string: Importando a string lowercase, que contém todas as letras minúsculas do alfabeto, e dando a ela o nome de lc.
from string import ascii_lowercase as lc
#Usando o argumento passado na linha de comando (sys.argv[1]) como um nome de arquivo. Read() transforma o conteúdo do arquivo em string e lower() passa todas as letras para minúsculas
file = open(sys.argv[1],'r').read().lower()
#Esse for executa 26 vezes. Uma para cada letra do alfabeto
for key in range(1,26):
    result = ''
#Imprimindo o valor da chave atual.
print ('Key:'), key
#Um for para cada caractere do texto a ser cifrado
for lt in file:
#Se esse caractere for uma letra
    if lt in lc:
#Encontra a posição da letra na string lc
        idx = lc.find(lt)
#Faz a subtração da posição da letra do texto com a chave
        idx = (idx - key) % 26
#Concatena o resultado junto com os anteriores
    result += lc[idx]
#Se não for uma letra
else:
#Joga o caractere na variável result
    result += lt
print (result)