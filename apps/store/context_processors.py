from .models import Category
from django.conf import settings # import the settings file

def menu_categories(request):
    categories = Category.objects.all()
    return {'menu_categories': categories}

def product_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MEDIA_URL': settings.MEDIA_URL}