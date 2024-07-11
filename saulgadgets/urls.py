"""
URL configuration for saulgadgets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
#from django.templatetags.static import static
from django.urls import path
from apps.cart.views import cart_detail
from apps.core.views import frontpage,contact,about
from apps.store.views import product_detail,category_detail,brand_detail, model_detail
from apps.store.api import api_add_to_cart, api_remove_from_cart

urlpatterns = [

    path('',frontpage,name='frontpage'),

    path('admin/',admin.site.urls),
    path('contact',contact,name='contact'),

    path('about',about,name='about'),
    path('cart_detail/',cart_detail,name='cart_detail'),

    # API endpoints
    path('api/add_to_cart/', api_add_to_cart, name='api_add_to_cart'),  # Add product to cart
    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),  # Remove product from cart

    # Add more API endpoints as needed...

    # Store URLs
    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),
    path('<slug:slug>/', brand_detail, name='brand_detail'),
    path('<slug:slug>/', model_detail, name='model_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #

# import debug_toolbar
    # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    # Debug toolbar settings
    # DEBUG_TOOLBAR_CONFIG = {
    #     'DISABLE_PANELS': ['debug_toolbar.panels.redirects.RedirectsPanel'],
    # }
     # DEBUG_TOOLBAR_ENABLE = True
     # DEBUG_TOOLBAR_PATCH_SETTINGS = False
     # DEBUG_TOOLBAR_SHOW_TOOLBAR_CALLBACK = lambda request: settings.DEBUG
     # DEBUG_TOOLBAR_PANELS = [
     #     'debug_toolbar.panels.versions.VersionsPanel',
     #     'debug_toolbar.panels.timer.TimerPanel',
     #     'debug_toolbar.panels.settings.SettingsPanel',
     #     'debug_toolbar.panels.headers.HeadersPanel',
     #     'debug_toolbar.panels.request.RequestPanel',
     #     'debug_toolbar.panels.sql.SQLPanel',
     #     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
     #     'debug_toolbar.panels.templates.TemplatesPanel',
     #     'debug_toolbar.panels.cache.CachePanel',
     #     'debug_toolbar.panels.signals.SignalsPanel',
     #     'debug_



print("MEDIA_URL  ::::" + str(settings.MEDIA_URL)  )
print("MEDIA_ROOT  ::::" + str(settings.MEDIA_ROOT)  )