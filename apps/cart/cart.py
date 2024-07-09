from django.conf import settings
from django.shortcuts import get_object_or_404

from apps.store.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            self.session[settings.CART_SESSION_ID] = cart = {}
        self.cart = cart
    def __iter__(self):
        print('itering the cart..')
        product_ids = self.cart.keys()
        product_clean_ids = []
        for p in product_ids:
            product_clean_ids.append(p)
            product = get_object_or_404(Product, id=int(p))
            self.cart[str(p)]['product'] =  product
            self.cart[str(p)]['title'] = product.title  # set the product title
            self.cart[str(p)]['price'] = float(product.price)  # set the product price

        for item in self.cart.values():
           # print('item ::::', item)
            item['price'] = float(item['price'])
            item['total_price'] = float(item['price'] * item['quantity'])  # calculate the total price for each item
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def count(self):
        return len(self)

    def add_to_cart(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)  # convert the product id to string
        if product_id not in self.cart:
            product = get_object_or_404(Product, id=product.id)
            self.cart[product_id] = {'quantity': 0, 'price': float(product.price),
                                     'id': product_id}  # initialize the product with quantity and price
            self.cart[product_id]['title'] = product.title  # set the product title
        print("cart after adding ::  ", self.cart)
        print("update_quantity",update_quantity)
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity  # update the quantity if update_quantity is True
        else:
            self.cart[product_id]['quantity'] += quantity  # add the quantity if update_quantity is False (default)
        self.save()
        print("cart after save cart ::  ", self.cart)

    def remove(self, product_id):
        print('removing product from cart..')
        print("product_id", product_id)
        print("cart before removing ::  ", self.cart.keys())
        if product_id in self.cart:
            print("product_id", product_id)
            del self.cart[product_id]  # remove the product from the cart
            print("product_id {} deleted : ".format(product_id))
            self.save()  # save the cart in the session
            print("cart ::  ",self.cart)
        else:
            print("product {} not in cart".format(product_id ))

    def save(self):
        self.session.modified = True
        self.session[settings.CART_SESSION_ID] = self.cart  # save the cart in the session
        self.session[settings.CART_SESSION_COOKIE_AGE] = self.session.get(
            settings.CART_SESSION_COOKIE_AGE) or 0  # update the session expiration time
        self.session.save()  # save the session
        return self.cart

    def get_total_length(self):
        return sum(int(item['quantity']) for item in self.cart.values())