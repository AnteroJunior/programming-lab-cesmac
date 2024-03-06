def show_message(number_1, number_2):
	print(f'{number_1} + {number_2} = {number_1 + number_2}')	

def another_sum():
	user_choice = input('Deseja realizar mais uma soma? [S ou N] ')
	print(f'Resposta: {user_choice}')
	while user_choice == 'S' or user_choice == 's':
		number_1 = int(input('Digite um número: '))
		number_2 = int(input('Digite outro número: '))
		show_message(number_1, number_2)
		user_choice = input('Deseja realizar mais uma soma? [S ou N] ')
		print(f'Resposta: {user_choice}')

def main():
	print("Operação - Adição!")

	number_1 = int(input('Digite um número: '))
	number_2 = int(input('Digite outro número: '))
	show_message(number_1, number_2)

	another_sum()

main()