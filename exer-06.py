#Escreva um programa que recebe uma string e conta aquantidade de vogais (a, e, i, o, u)
#presentes nela

def contar_vogais(string):
    contador = 0
    string = string.lower()
    
    for caractere in string:
        if caractere in 'aeiou':
            contador += 1
            
    return contador

entrada = input('Digite uma string: ')

quantidade_vogais = contar_vogais(entrada)

print('A quantidade de vogais na string é:', quantidade_vogais)