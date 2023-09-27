#ESscreva um programa que recebe um número interio positivo e calcula a soma dos seus 
#dígitos.

numero = int(input('Digite um número inteiro positivo: '))

if numero < 0:
    print('Por favor digite um numero inteiro positivo')
else:
    soma_digitos = 0
    numero_str = str(numero)
    
    for digito in numero_str:
         soma_digitos += int(digito)
    print('A soma dos dígitos de' , numero, 'é', soma_digitos)