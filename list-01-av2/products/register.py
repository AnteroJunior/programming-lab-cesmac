products_list = []

def register_product():
    name = ''
    price = 0.00

    while(name == ''):
        name = input('Informe o nome do produto: ')
    
    while(price == 0.00):
        price = input('Informe o preço do produto: ')

    products_list.append({
        'name': name,
        'price': price
    })
    print('Produto cadastrado com sucesso!')