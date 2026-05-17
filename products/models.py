from django.db import models


class Products(models.Model):

    GENDER_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Unisex', 'Unisex'),
    ]

    CLOSURE_CHOICES = [
        ('Lace-Up', 'Lace-Up'),
        ('Slip-On', 'Slip-On'),
        ('Velcro', 'Velcro'),
        ('Zipper', 'Zipper'),
        ('Buckle', 'Buckle'),
    ]

    # Basic Product Info
    api_id = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Main Product Image
    image = models.URLField()

    category = models.CharField(max_length=100)

    rating = models.FloatField(default=0)

    # =========================
    # SIZING
    # =========================

    # Example: [6,7,8,9,10]
    sizes = models.JSONField(default=list, blank=True)

    # =========================
    # MATERIAL / OUTER LAYER
    # =========================

    material = models.CharField(max_length=150, blank=True)
    texture = models.CharField(max_length=100, blank=True)
    finish = models.CharField(max_length=100, blank=True)

    # =========================
    # FEATURES
    # =========================

    # Example:
    # ["Air Max Cushioning", "Breathable Mesh"]
    features = models.JSONField(default=list, blank=True)

    closure_type = models.CharField(
        max_length=50,
        choices=CLOSURE_CHOICES,
        blank=True
    )

    sole_type = models.CharField(max_length=100, blank=True)

    waterproof = models.BooleanField(default=False)

    # Weight per shoe in grams
    weight_grams = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    # =========================
    # EXTRA FIELDS
    # =========================

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='Unisex'
    )

    # Example:
    # ["Daily Running", "Street Wear"]
    best_for = models.JSONField(default=list, blank=True)

    in_stock = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# =========================================
# PRODUCT COLOR VARIANTS
# =========================================

class ProductColor(models.Model):

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='colors'
    )

    # Example: Black, White, Red
    name = models.CharField(max_length=50)

    # Example: #000000
    hex = models.CharField(max_length=7)

    # Image for this specific color
    image = models.URLField()

    def __str__(self):
        return f"{self.product.name} - {self.name}"