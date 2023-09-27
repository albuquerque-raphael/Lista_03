#Crie uma função que verifica se uma palavra ou frase é palíndromo (lê-se igual de trás para frente,
# desconsiderando espaços e pontuação).

import re

def palindromo(frase):
    frase  = re.sub(r'[^\w\s]', '', frase)
    frase = frase.lower()
    return frase == frase [::-1]

frase1 = 'radar'
frase2 = 'ovo'
frase3 = 'reger'

print(palindromo(frase1))
print(palindromo(frase2))
print(palindromo(frase3))