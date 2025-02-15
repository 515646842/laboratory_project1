from django.contrib import admin

from products.models import ProductCategory, Product, Basket
# Register your models here.

admin.site.register(ProductCategory)


# admin.site.register(Basket)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category',]
    fields = ['image', 'name', 'description', ('price', 'quantity'), 'category',]
    search_fields = ['name',]
    ordering = ['name',]


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity',]
    extra = 0