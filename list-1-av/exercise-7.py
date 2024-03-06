questions = [
    'Telefonou para a vítima? ',
    'Esteve no local do crime? ',
    'Mora perto da vítima? ',
    'Devia para a vítima? ',
    'Já trabalhou com a vítima? '
]

positiveAnswers = 0
actualQuestion = 0

while(actualQuestion < len(questions)):
    answer = input(questions[actualQuestion])
    print(answer)
    match answer:
        case 'S' | 's':
            positiveAnswers += 1
            actualQuestion += 1
        case 'N' | 'n':
            actualQuestion += 1
        case _:
            print('Insira uma resposta válida (S/s, N/n)')
            pass
        
if(positiveAnswers == 2):
    print('Suspeita')
elif(positiveAnswers == 3 or positiveAnswers == 4):
    print('Cúmplice')
elif(positiveAnswers == 5):
    print('Assassino')
else:
    print('Inocente')