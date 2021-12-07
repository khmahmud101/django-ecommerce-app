from django.urls import path
from shop import views
app_name = 'shop'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
]