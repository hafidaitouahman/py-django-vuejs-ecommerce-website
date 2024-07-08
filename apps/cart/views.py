from django.shortcuts import render
from .cart import Cart
# Create your views here.

def cart_detail(request):
    cart = Cart(request)
    print ('cart ::::' + str(cart))
    productsstring = ''
   # for item in cart:
    #    productsstring += "{'id':'%s', 'title':'%s', 'quantity':'%s', 'price':'%s','total_price':'%s'}" % (item['id'], item['title'], item['quantity'], item['price'], item['total_price']) + ','

    #print('productsstring ::::' + productsstring)
    #products: {{productsstring | safe}}
    context = {
        'cart': cart,
        #'productsstring': productsstring
    }
    return render(request,'cart_detail.html', context)