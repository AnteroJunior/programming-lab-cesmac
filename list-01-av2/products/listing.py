from products.register import products_list

def list_products():
    for product in products_list:
        print('------------------------')
        print(f'Produto: {product['name']}')
        print(f'Preço: {product['price']}')
        print('------------------------')