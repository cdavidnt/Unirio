# Alunos: Carlos David Carvalho Barbosa Neto e Augusto Tavares Nasser

from re import *

# Modifique o trecho daqui

quantia = r"^R\$([1-9]\d*|0)(,\d\d)?$"
bissexto = r"^(19\d(0|2|6)|20\d(4|8))$"
dna = r"^(A|C|T|G)+$"
comentario = r"^/\*([^*]*\*+[^/\*]+)*[^*]*\*+/$"
gene = r"^(ATG|GTG|TTG)((A|C|G)(A|C|T|G){2}|T(T|C)(A|G|T|C)|(TA(C|T)|TG(C|T|G)))*(TGA|TAA|TAG)$"

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
    
    