import json
import os

from .models import Products, ProductColor


def fetch_data():

    file_path = os.path.join(
        os.path.dirname(__file__),
        'products.json'
    )

    try:

        with open(file_path, 'r', encoding='utf-8') as f:
            products = json.load(f)

        print("📦 Products loaded:", len(products))

        # DELETE OLD DATA
        ProductColor.objects.all().delete()
        Products.objects.all().delete()

        for item in products:

            product = Products.objects.create(

                api_id=item.get('api_id'),

                name=item.get('name'),

                description=item.get('description'),

                price=item.get('price'),

                image=item.get('image'),

                category=item.get('category'),

                rating=item.get('rating', 0),

                # NEW FIELDS

                gender=item.get('gender', 'Unisex'),

                in_stock=item.get('in_stock', True),

                best_for=item.get('best_for', []),

                sizes=item.get('sizes', []),

                closure_type=item.get('closure_type'),

                sole_type=item.get('sole_type'),

                waterproof=item.get('waterproof', False),

                weight_grams=item.get('weight_grams'),

                material=item.get('material'),

                texture=item.get('texture'),

                finish=item.get('finish'),

                features=item.get('features', [])
            )

            # SAVE COLORS

            colors = item.get('colors', [])

            for color in colors:

                ProductColor.objects.create(
                    product=product,

                    name=color.get('name'),

                    hex=color.get('hex'),

                    image=color.get('image')
                )

        print("✅ Products Imported Successfully")

    except Exception as e:

        print("❌ ERROR:", e)