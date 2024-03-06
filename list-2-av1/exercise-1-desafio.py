import sys
sys.setrecursionlimit(1500)

LIMIT = 500

def fibonacci(number):
	if number == 0:
		return 0
	elif number == 1:
		return 1
	else:
		return fibonacci(number - 1) + fibonacci(number - 2)


contador = 1
while True:
	if(fibonacci(contador) <= LIMIT):
		print(fibonacci(contador))
	else:
		print(fibonacci(contador))
		break
	contador += 1