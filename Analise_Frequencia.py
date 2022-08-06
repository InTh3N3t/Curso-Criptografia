#!/usr/bin/env python
#Biblioteca sys: Requisito para a passagem de parâmetros na linha de comando
import sys
#Biblioteca string: Importando a string uppercase, que contém todas as letras maiúsculas do alfabeto, e dando a ela o nome de uc.
from string import uppercase as uc
#Essa string contém todas as letras do alfabeto na ordem de maior aparição no idioma inglês
enfreq = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
#Esse dicionário contém todas as letras do alfabeto ao lado de um número. Esse número servirá para contar quantas vezes cada uma aparece no texto.
ltcount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
#Abertura do arquivo passado como primeiro argumento
file = open(sys.argv[1],'r').read().upper()
#Executa uma vez para cada caractere do alfabeto
for lt in file:
#Se o caractere for uma letra
 if lt in uc:
#O valor referente a essa letra recebe mais 1
ltcount[lt] += 1
order = []
score = 0
#Coloca o dicionário em ordem decrescente de valoresfor w in sorted(ltcount, key=ltcount.get, reverse=True):
print w, ltcount[w]
order.append(w)
#Transforma a lista order em uma string
order = ''.join(order)
#Verifica se as seis letras mais comuns do texto batem com as 6 primeiras da string enfreq
for clt in enfreq[:6]:
if clt in order[:6]:
#Caso positivo, a variável score recebe mais 1
score += 1
#O mesmo para as 6 letras que menos aparecem
for ult in enfreq[-6:]:
if ult in order[-6:]:
score += 1
#A variável score guarda quantas letras batem com as letras mais comuns e menos comuns da string enfreq
print 'Score:', score, 'out of 12'