#Escreva uma função que gere uma sequencia Fibonacci até um determinado número
#de termos especificado pelo usuário.

def gerar_fibonacci(numero_de_termos):
    
    fibonacci = []
    
    a, b = 0, 1

    fibonacci.append(a)
    fibonacci.append(b)

    for _ in range(2, numero_de_termos):
        
        c = a + b
        fibonacci.append(c)

        a, b = b, c

    return fibonacci


numero_de_termos = int(input("Digite o número de termos da sequência de Fibonacci desejado: "))


sequencia = gerar_fibonacci(numero_de_termos)


print("Sequência de Fibonacci:")
for termo in sequencia:
    print(termo, end=" ")