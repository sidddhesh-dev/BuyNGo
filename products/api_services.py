import requests
from .models import Products

API_URL = "https://dummyjson.com/products?limit=100"


def fetch_data():
    try:
        response = requests.get(API_URL)

        if response.status_code != 200:
            print("❌ API request failed")
            return

        data = response.json()

        products = data.get("products", [])

        if not products:
            print("❌ No products found in API")
            return

        # 🔥 Optional: Clear old data
        Products.objects.all().delete()

        count = 0

        for item in products:
            title = item.get("title", "").lower()
            category = item.get("category", "").lower()

            # 🔥 FILTER ONLY SHOES
            if (
                "shoe" in title or
                "sneaker" in title or
                "footwear" in category
            ):
                Products.objects.create(
                    api_id=item.get("id"),
                    name=item.get("title", ""),
                    description=item.get("description", ""),
                    price=item.get("price", 0),
                    image=item.get("thumbnail", ""),
                    category=category,
                    rating=item.get("rating", 0),
                )

                print("✅ Added:", item.get("title"))
                count += 1

        print(f"\n🔥 {count} shoes imported successfully")

    except Exception as e:
        print("❌ Error:", str(e))