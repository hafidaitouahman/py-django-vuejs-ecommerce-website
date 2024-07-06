from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# from django_autoslug.fields import AutoSlugField
from django.forms import ModelForm

import uuid


# Create your models here.

def defaultSlug():
    slug = (AutoSlugField(populate_from='title', editable=True))
    return (slug if slug else uuid.uuid1)


CATEGORY_STATUS = models.TextChoices(
    "Display", (
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    )
)


class CategoryStatusChoice(models.TextChoices):
    ACTIVE = u'A', 'Active'
    INACTIVE = u'I', 'Iactive'


class Category(models.Model, ):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, max_length=255, unique=True, default=uuid.uuid1, verbose_name='URL Slug')
    status = models.CharField(max_length=2, blank=True, null=True, choices=CategoryStatusChoice.choices,
                              default=CategoryStatusChoice.ACTIVE)
    ordering = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        """ 
        this is a multi-line comment
        # db_table = 'Category'
        """
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    # def slug(self):
    #    return slugify(self.title)
    def __str__(self):
        return self.title


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["title", "status"]


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, default=uuid.uuid1, verbose_name='URL Slug')
    # slug = AutoSlugField(populate_from=lambda instance: instance.title,
    #                      unique_with=['category'],
    #                     slugify=lambda value: value.replace(' ','-'), editable=True)
    description = models.TextField(blank=True, null=True, max_length=255)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # , unique=True, default=AutoSlugField(populate_from='title', editable=True)

    class Meta:
        """ 
        this is a multi-line comment
        # db_table = ''
        """
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    # def slug(self):
    #    return slugify(self.title)
    def __str__(self):
        return self.title


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["category", "title", "description", "price"]
