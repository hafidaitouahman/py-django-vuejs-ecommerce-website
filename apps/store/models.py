from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
#from django_autoslug.fields import AutoSlugField

import uuid

# Create your models here.

def defaultSlug():
    slug = (AutoSlugField(populate_from='title', editable=True))
    return (slug if slug else uuid.uuid1)
    
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, default=uuid.uuid1,verbose_name='URL Slug')
 
    
    
    
   # def save(self, *args, **kwargs):
   #     self.slug = AutoSlugField(populate_from='title', editable=True)
   #     super().save(*args, **kwargs)
        
    class Meta:
        """ 
        this is a multi-line comment
        # db_table = 'Category'
        """
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    #def slug(self):
    #    return slugify(self.title)
    def __str__(self):
        return self.title
    
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, default=uuid.uuid1,verbose_name='URL Slug')
    #slug = AutoSlugField(populate_from=lambda instance: instance.title,
   #                      unique_with=['category'],
    #                     slugify=lambda value: value.replace(' ','-'), editable=True)
    description = models.TextField(blank=True,null=True, max_length=255)
    price = models.FloatField()
    #, unique=True, default=AutoSlugField(populate_from='title', editable=True)
    
    class Meta:
        """ 
        this is a multi-line comment
        # db_table = ''
        """
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    #def slug(self):
    #    return slugify(self.title)
    def __str__(self):
        return self.title