grade1 = float(input('Informe a primeira nota: '))
grade2 = float(input('Informe a segunda nota: '))

media = (grade1 + grade2) / 2

if(media == 10):
    print('Aprovado com Distinção')
elif(media >= 7):
    print('Aprovado')
else:
    print('Reprovado')