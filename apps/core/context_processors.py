from django.conf import settings # import the settings file

def product_media(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'MEDIA_URL': settings.MEDIA_URL}