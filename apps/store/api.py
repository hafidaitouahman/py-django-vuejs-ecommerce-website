from django.http import JsonResponse
from apps.cart.cart import Cart
from .models import Product
from django.shortcuts import get_object_or_404
import json

def api_add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = str(data['product_id'])
        print ('data ::::' + str(data))
        print('product_id ::::' + product_id)

        product = get_object_or_404(Product, id=product_id)
        update = data['update']
        quantity = int(data['quantity'])
        print('quantity ::::' + str(quantity))
        cart = Cart(request)
        if update:
            cart.add_to_cart(product=product, quantity=quantity, update_quantity=True)
        else:
            cart.add_to_cart(product=product, quantity=quantity, update_quantity=False)

        return JsonResponse({'success': True, 'count': cart.count()})
    return JsonResponse({'success': False})  # Return an empty cart on failure

def api_remove_from_cart(request):
    print("api_remove_from_cart called..")
    if request.method == 'POST':
        data = json.loads(request.body)
        print('data ::::' + str(data))
        product_id = str(data['product_id'])
        cart = Cart(request)
        cart.remove(product_id)
        return JsonResponse({'success': True, 'count': cart.count()})
    return JsonResponse({'success': False})  # Return an empty cart on failure