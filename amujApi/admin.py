from django.contrib import admin
from .models import Collection, Product, Size, ProductImage

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(ProductImage)
