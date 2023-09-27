#Escreva um programa que receba cinco notas de um aluno e clacule a média.
#Em seguida, exiba se o aluno foi aprovado (média maior ou igual a 7), ou
#reprovado (media menor que 7).

aluno = str(input('Qual é seu nome: '))
nota1 = float(input('Qual foi a sua primeria nota: '))
nota2 = float(input('Qual foi a sua segunda nota: '))
nota3 = float(input('Qual foi a sua terceira nota: '))
nota4 = float(input('Qual foi a sua quarta nota: '))
nota5 = float(input('Qual foi a sua quinta nota: '))
media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
if media >= 7:
    print('{} você passou por média com nota {}. Parabéns'.format(aluno, media))
else:
    print('{} você ficou com a média {}, está reprovado. Não foi dessa vez.'.format(aluno,media))
    