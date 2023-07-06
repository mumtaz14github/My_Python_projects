from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
    lisr_per_page = 2


admin.site.register(Product, ProductAdmin)