from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Категория """

    prepopulated_fields = {'slug': ('name',)}
    list_display = ("id", "name", "slug", "get_image")
    list_display_links = ("id", "name")
    save_as = True
    fields = ("name", "slug", "image", "get_image")
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        """Отобразим фото в админке"""

        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        else:
            return f'Image not set'

    get_image.short_description = 'Image'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Товары """

    prepopulated_fields = {'slug': ('name',)}
    list_display = (
        "id", "name", "category", "price", "discount_price", "created_at", "get_image"
    )
    list_display_links = ("id", "name",)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
    fields = (
        "name", "slug", "description", "category", "price", "discount_price", "created_at",
        "updated_at", "image", "get_image",
    )
    readonly_fields = ('get_image', "created_at", "updated_at",)
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        """Отобразим фото в админке"""

        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        else:
            return f'Image not set'

    get_image.short_description = 'Image'
