from django.urls import path
from shop import views
app_name = 'shop'
urlpatterns = [
    path('', views.Home, name='home'),
    
    path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('category/<name>',views.category, name="category"),
    #path('category/',views.Category, name="category"),
]