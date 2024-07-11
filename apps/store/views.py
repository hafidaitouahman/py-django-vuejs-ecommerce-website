from django.shortcuts import render,get_object_or_404
from .models import Product,Category,Brand, Model
# Create your views here.

def product_detail(request,category_slug,slug):
    product = get_object_or_404(Product,slug=slug)
    context = {
        'product': product
    }
    return render(request,'product_detail.html',context)

def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request,'category_detail.html',context)

def brand_detail(request,slug):
    brand = get_object_or_404(Brand, slug=slug)
    context = {
        'brand': brand
    }
    return render(request, 'brand_detail.html', context)

def model_detail(request,slug):
    model = get_object_or_404(Model, slug=slug)
    context = {
        'model': model
    }
    return render(request, 'model_detail.html', context)
