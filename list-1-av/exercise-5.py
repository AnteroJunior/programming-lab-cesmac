number1 = float(input('Informe o primeiro número: '))
number2 = float(input('Informe o segundo número: '))
number3 = float(input('Informe o terceiro número: '))

numberList = [number1, number2, number3]
numberList.sort()

print(f"O maior é {numberList[2]}")