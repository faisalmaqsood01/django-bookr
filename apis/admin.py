from django.contrib import admin
from .models import Product, CartItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ adding the product class to the admin site """

    list_display = (
        'name', "price", "quantity", 'created', 'updated_at')

    search_fields = ["name"]
    date_hierarchy = "created"
    list_editable = ['price', 'quantity']


admin.site.register(CartItem)
