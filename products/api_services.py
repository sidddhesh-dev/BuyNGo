import json
import os
from .models import Products

def fetch_data():
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'products.json')

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

   
        products = data  

        if not products:
            print("❌ No products found in JSON")
            return

        # clear old data
        Products.objects.all().delete()

        count = 0

        for item in products:
            Products.objects.create(
                api_id=item.get('api_id'),
                name=item.get('name'),
                description=item.get('description'),
                price=item.get('price'),
                image=item.get('image'),
                category=item.get('category'),
                rating=item.get('rating'),
            )
            count += 1

        print(f"✅ {count} products inserted successfully")

    except Exception as e:
        print("❌ Error:", e)