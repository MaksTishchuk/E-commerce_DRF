from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):
    """ Модель заказа """

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=15)
    additional_information = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    """ Товар в заказе """

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id} - {self.order} - {self.product}'
