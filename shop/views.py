from django.shortcuts import render

# Import views
from django.views.generic import ListView, DetailView

# Models
from shop.models import Product

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class Home(ListView):
    model = Product
    template_name = 'shop/home.html'

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shop/product_detail.html'