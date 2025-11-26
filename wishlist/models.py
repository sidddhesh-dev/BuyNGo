from django.db import models
from django.db import models
from django.contrib.auth.models import User
from products.models import Products

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # no duplicates

    def __str__(self):
        return f"{self.user.username} -> {self.product.name}"

