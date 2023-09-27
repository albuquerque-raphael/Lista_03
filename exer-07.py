#Crie uma função que clacule o IMC(Indice de Massa Corporal) de uma pessoa,
#com base na sua altura e peso.

def calcular_imc(peso,altura):
    if altura < 1:
        raise ValueError('A altura deve ser fornecida em metros')
    
    imc = peso / (altura ** 2 )
    
    return imc

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em Metros: '))

imc = calcular_imc(peso, altura)

print('Seu IMC é:', imc)