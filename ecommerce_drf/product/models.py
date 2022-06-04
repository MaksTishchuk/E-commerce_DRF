from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image


class Category(models.Model):
    """ Модель категорий """

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='category/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Получим URL нашей категории """
        return f'/{self.slug}/'

    def get_image(self):
        """ Получим URL нашего изображения категории """
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Product(models.Model):
    """ Модель товаров """

    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_img/%Y/%m/%d/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='product_thumb/%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """ Получим URL нашего товара """
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        """ Получим URL нашего изображения товара """
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        """ Получим URL миниатюры нашего товара """
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        """ Сделаем миниатюру нашего изображения товара """
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail
