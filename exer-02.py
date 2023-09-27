#Escreva uma função que calcule a fatorial de um número inteiro positivo fornecido pelo usuário.

def calcular_fatorial(x):
    if x < 0:
        return 'Só a números positivos'
    elif x == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, x + 1):
            fatorial *= i
        return fatorial
    
numero = int(input('Digite um número inteiro e positivo: '))

resultado = calcular_fatorial(numero)
print('O fatorial de {} é {}'.format(numero, resultado))