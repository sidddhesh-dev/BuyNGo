from django.urls import path
from . import views

urlpatterns = [
    path("import/", views.import_products, name="import_products"),
    path("product/", views.product_list, name="product_list"),
    path("<int:id>/", views.product_details, name="product_detail"),
    path("import_success",views.import_products,name="import_success")
]
