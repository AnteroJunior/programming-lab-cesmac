gradesSum = 0
gradesInserted = 0

while gradesInserted < 3:
    grade = float(input(f"Informe a nota {gradesInserted + 1}: "))
    if(grade >= 0):
        gradesSum += grade
        gradesInserted += 1
    else:
        print('A nota deve ser maior ou igual a zero')
        pass

print(f"A média das 3 notas é {gradesSum / 3}")