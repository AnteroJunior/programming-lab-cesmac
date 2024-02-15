turno = input('Qual é o seu turno de estudo? (M, V, N): ')

while(turno not in ['M', 'V', 'N']):
    turno = input('Qual é o seu turno de estudo? (M, V, N): ')
    
match turno:
    case 'M':
        print('Bom Dia!')
    case 'V':
        print('Boa Tarde!')
    case 'N':
        print('Boa Noite!')
    case _:
        print('Valor Inválido!')    