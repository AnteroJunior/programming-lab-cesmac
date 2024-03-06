def check_for_divisors(number):
	for i in range(2, number):
		if(number % i == 0):
			return False

	return True


def main():
	isPrime = int(input('Informe o número a ser analisado: '))
	print('É primo' if check_for_divisors(isPrime) else 'Não é primo.')

main()