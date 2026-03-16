from django.db import models
from products.models import Products

class CartItem(models.Model):

    session_key = models.CharField(max_length=40, null=True, blank=True)

    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"