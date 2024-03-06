def validate_informations(obj):
	obj_value = obj['value']
	match(obj['validator']):
		case 'NOME':
			return True if len(obj_value) >= 3 and not any(char.isdigit() for char in obj_value) else False
		case 'IDADE':
			return True if int(obj_value) and int(obj_value) >= 0 and int(obj_value) <= 150 else False
		case 'SALARIO':
			return True if float(obj_value) > 0 else False
		case 'SEXO':
			return True if obj_value.lower() in ['f', 'm'] else False
		case 'STATUS':
			return True if obj_value.lower() in ['s', 'c', 'v', 'd'] else False


def main():
	list_validation = [
		{ 'value': None, 'validator': 'NOME', 'hint': 'Deve ser maior que 3 caracteres e não conter dígitos' }, 
		{ 'value': None, 'validator': 'IDADE', 'hint': 'Deve ser entre 0 e 150' }, 
		{ 'value': None, 'validator': 'SALARIO', 'hint': 'Deve ser maior que 0.00' }, 
		{ 'value': None, 'validator': 'SEXO', 'hint': 'Deve ser f ou m' }, 
		{ 'value': None, 'validator': 'STATUS', 'hint': 'Deve ser s, c, v ou d' }
	]

	index = 0
	
	while index < len(list_validation):
		list_validation[index]["value"] = input(f'Digite a informação {list_validation[index]["validator"].lower()}: ')
		if(validate_informations(list_validation[index])):
			print('Informação validada com sucesso.')
			index += 1
		else:
			print('Verifique o valor indicado e tente novamente.')
			print(list_validation[index]['hint'])
			pass

main()