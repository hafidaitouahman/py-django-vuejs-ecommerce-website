from django.shortcuts import render
from .cart import Cart
import json
# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    print ('cart ::::' + str(cart))
    productsstring = ''
    for item in cart:
        product = "{'id':'%s', 'title':'%s', 'quantity':'%s', 'price':'%s','total_price':'%s'}," % (item['id'], item['title'], item['quantity'], item['price'], item['total_price'])
        productsstring += product

    context = {
        'cart': cart,
        'productsstring': productsstring.rstrip(',')
    }
    return render(request,'cart_detail.html', context)