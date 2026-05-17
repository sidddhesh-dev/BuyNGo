import json


# LOAD JSON FILE
with open('products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for product in products:

    colors = product.get('colors', [])

    if colors:
        product['image'] = colors[0].get('image', '')


with open('products_updated.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=4)

print('✅ products_updated.json created successfully')