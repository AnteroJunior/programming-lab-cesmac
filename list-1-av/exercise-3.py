letter = input('Informe uma letra: ')
vowels = ['a', 'e', 'i', 'o', 'u']

while(len(letter) > 1 or len(letter) == 0):
    letter = input('Informe uma letra: ')

if(letter in vowels):
    print('É uma vogal')
else:
    print('É consoante')