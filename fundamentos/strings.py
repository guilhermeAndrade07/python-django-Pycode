# FUNDAMENTOS DE STRING
texto = 'AULA PYCODEBR'
print(texto[0]) # A
print(texto[0:4]) # AULA
print(texto[5:13]) # PYCODEBR
print(len(texto)) # 13

print(texto.count('A')) # 2

print(texto.capitalize()) # Aula pycodebr
print(texto.title()) # Aula Pycodebr

print(texto.split()) # ['AULA', 'PYCODEBR']

lista_de_palavras = texto.split()
print(''.join(lista_de_palavras)) # AULAPYCODEBR
print(' '.join(lista_de_palavras)) # AULA PYCODEBR

texto2 = '    AULA PYCODEBR    '
print(texto2)
print(texto2.strip())
print(texto2.rstrip())
print(texto2.lstrip())