from django.contrib import admin
from .models import Collection, Product, Size, ProductImage

# Register your models here.
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(ProductImage)


# editting
admin.site.site_header = "Amuj Admin"
admin.site.site_title = "Amuj Admin Portal"
admin.site.index_title = "Welcome to Amuj admin"
