from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Заказ """

    list_display = ("id", "user", "first_name", "email", "phone", "created_at", "order_price")
    list_display_links = ("id", "user", "first_name")
    save_as = True
    fields = (
        "user",
        "first_name",
        "last_name",
        "middle_name",
        "email",
        "phone",
        "country",
        "city",
        "address",
        "zipcode",
        "additional_information",
        "created_at",
        "order_price",
    )
    readonly_fields = ('created_at',)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """ Товар из заказа """

    list_display = ("id", "order", "product", "price", "quantity",)
    list_display_links = ("id", "order", "product")
    save_as = True
    fields = (
        "order",
        "product",
        "price",
        "quantity",
    )
