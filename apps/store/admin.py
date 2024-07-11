from django.contrib import admin


# Register your models here.
from .models import Category,Product, Brand, Model

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(Brand)

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("brandName", "name")