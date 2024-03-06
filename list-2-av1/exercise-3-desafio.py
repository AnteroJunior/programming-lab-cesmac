def validate_number(message):
	number = int(input(message))
	
	while number < 0 or number > 1000:
		number = int(input(message))
	
	return number

def final_values(user_list):
	user_list.sort()
	menor = user_list[0]
	maior = user_list[-1]
	soma = sum(user_list)
	return menor, maior, soma

def main():
	total_numbers = int(input('Informe quantos números você vai digitar: '))
	user_list = []

	contador = 0
	while contador < total_numbers:
		user_list.append(validate_number(f'Informe o número {contador + 1}: '))
		contador += 1
	menor, maior, soma = final_values(user_list)
	print(f'MAIOR: {maior}\nMENOR: {menor}\nSOMA: {soma}')


main()