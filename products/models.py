from django.db import models

class Products(models.Model):
    api_id = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField()  # storing image URL directly
    category = models.CharField(max_length=100)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name



