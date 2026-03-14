from django.urls import path
from . import views

urlpatterns = [

    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_details, name='product_details'),
    path('import-products/', views.import_products, name='import_products'),
    path('search/', views.search_products, name='search_products'),

]
