import json
import os
from .models import Products

def fetch_data():
    print("🚀 FUNCTION CALLED")

    file_path = os.path.join(os.path.dirname(__file__), 'products.json')
    print("📂 File path:", file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            products = json.load(f)

        print("📦 Products loaded:", len(products))

        Products.objects.all().delete()

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

        print("✅ INSERT DONE")

    except Exception as e:
        print("❌ ERROR:", e)