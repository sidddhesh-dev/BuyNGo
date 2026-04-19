from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('developer/', views.developer, name='developer'),
      path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('developer/', views.developer, name='developer'),
]