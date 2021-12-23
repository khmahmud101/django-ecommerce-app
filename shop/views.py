from django.shortcuts import render, get_object_or_404

# Import views
from django.views.generic import ListView, DetailView

# Models
from shop.models import Product, Category

# Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.




def Home(request):
    products = Product.objects.all()
    #cat = get_object_or_404(Category,"Cloths")
    #catproducts=Product.objects.filter(category=cat.id)
    categories = Category.objects.all()
    print(categories)
    
    
    return render(request,"shop/home.html",{ "products":products,"categories":categories})

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shop/product_detail.html'

# def Category(request):
#     cats = Category.objects.all()
#     return render(request,"navbar.html",{"cats":cats})

def category(request, name):
   
    #print(posts.category.title)
    cat = get_object_or_404(Category,title=name)
    products=Product.objects.filter(category=cat.id)
    
    
   
    return render(request,"shop/category.html",{"products":products,"cat":cat})



