import requests
from .models import Products

API_URL = "https://fakestoreapi.com/products"

def fetch_data():
    response = requests.get(API_URL)
    data = response.json()

    for item in data:
        Products.objects.update_or_create(
            api_id=item["id"],
            defaults={
                "name": item["title"],
                "description": item["description"],
                "price": item["price"],
                "image": item["image"],
                "category": item["category"],
                "rating": item["rating"]["rate"],
            }
        )
