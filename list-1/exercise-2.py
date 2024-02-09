productPrice = float(input("Informe o valor do produto: "))
PERCENTAGE = 15 # Caso seja necessário alterar o desconto posteriormente. DESCONTO DEVE SER ATÉ 100!
DISCOUNT = 1 - (PERCENTAGE / 100)
finalPrice = productPrice * DISCOUNT

print(f"O produto terá o valor de R$ {finalPrice} conforme o desconto de {PERCENTAGE}%")