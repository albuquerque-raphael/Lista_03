#Crie uma calculadora que realize oprações de adição, subtração, multiplicação e divisão,
#com base na escolha do usuário.

def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    else:
        return a / b

print("Escolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")


opcao = input("Digite o número da operação desejada: ")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if opcao == '1':
    resultado = adicao(numero1, numero2)
    operacao = "adição"
elif opcao == '2':
    resultado = subtracao(numero1, numero2)
    operacao = "subtração"
elif opcao == '3':
    resultado = multiplicacao(numero1, numero2)
    operacao = "multiplicação"
elif opcao == '4':
    resultado = divisao(numero1, numero2)
    operacao = "divisão"
else:
    resultado = "Opção inválida"
    operacao = ""


if operacao:
    print(f"O resultado da {operacao} é: {resultado}")
else:
    print(resultado)