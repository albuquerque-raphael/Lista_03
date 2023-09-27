#Crie uma função e verifique se um número é primo ou não.

def primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input('Digite um número: '))
if primo(numero):
    print(numero, 'É um número primo')
else:
    print(numero, 'Não é número primo')