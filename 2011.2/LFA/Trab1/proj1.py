# Alunos: Carlos David Carvalho Barbosa Neto e Augusto Tavares Nasser

from re import *

# Modifique o trecho daqui

quantia = r""
bissexto = r""
dna = r""
comentario = r""
gene = r""

# Ate aqui. Nao mude nada daqui para baixo!

while True:
  s = input()
  print(s)
  if search(quantia, s):
    print("Quantia em reais")
  if search(bissexto, s):
    print("Ano bissexto recente")
  if search(dna, s):
    print("Fragmento de DNA")
  if search(comentario, s):
    print("Comentario em C")
  if search(gene, s):
    print("Gene")
    
    