from django.db import models
from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# from django_autoslug.fields import AutoSlugField
from django.forms import ModelForm
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.utils.translation import gettext_lazy as _trans  # this is a translation for 'Text'






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

class Brand(models.Model, ):
    code = models.CharField(blank=True,max_length=25, unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, max_length=255, unique=True, default=uuid.uuid1, verbose_name='URL Slug')
    status = models.CharField(max_length=2, blank=True, null=True, choices=CategoryStatusChoice.choices,
                              default=CategoryStatusChoice.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name).lower()
        self.code = self.slug
        super().save(*args, **kwargs)

class Model(models.Model, ):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    code = models.CharField(blank=True,max_length=25, unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, max_length=255, unique=True, default=uuid.uuid1, verbose_name='URL Slug')
    status = models.CharField(max_length=2, blank=True, null=True, choices=CategoryStatusChoice.choices,
                              default=CategoryStatusChoice.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    ordering = models.IntegerField(default=0)

    def brandName(self):
        return self.brand.name
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name).lower()
        self.code = self.slug
        super().save(*args, **kwargs)

class Category(models.Model, ):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, max_length=255, unique=True, default=uuid.uuid1, verbose_name='URL Slug')
    status = models.CharField(max_length=2, blank=True, null=True, choices=CategoryStatusChoice.choices,
                              default=CategoryStatusChoice.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

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
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, default=uuid.uuid1, verbose_name='URL Slug')
    description = models.TextField(blank=True, null=True, max_length=255)
    product_no = models.CharField(max_length=25, blank=False, null=False)
    oem = models.CharField(max_length=25, blank=False, null=False)
    price = models.FloatField()
    is_featured = models.BooleanField(default=False)

    image = models.ImageField(upload_to='products/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='products/thumbnails/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)


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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.thumbnail = self.make_thumbnail(self.image)  # call the method to create thumbnail when product is saved.
        super().save(*args, **kwargs)


    def make_thumbnail(self,image,size=(300, 200)):
        if not image:
            return

        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = InMemoryUploadedFile(
            thumb_io, None, 'thumbnail_%s.jpg' % img, 'image/jpeg',
            thumb_io.tell(), None
        )

        self.thumbnail.save(thumbnail.name, thumbnail, save=False)
        #self.save()
        return thumbnail

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["category","brand","model","product_no","oem", "title", "description", "price", "image", "thumbnail", "is_featured"]
