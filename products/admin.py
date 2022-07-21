from django.contrib import admin

from .models import *

class ImageItemsInline(admin.TabularInline):
    model = Images
    extra = 0

class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color']
    inlines = [ImageItemsInline]

# Catalog
admin.site.register(ProdType)
admin.site.register(Catalog, ImageAdmin)
admin.site.register(Price)
admin.site.register(Images)
admin.site.register(Tags)
admin.site.register(Size)

# Advatages
admin.site.register(Advantages)

# Econom
admin.site.register(Econom)

# Furniture
admin.site.register(Furniture)
admin.site.register(FurnitureCategories)

# Pluses
admin.site.register(Pluses)

# Profit
admin.site.register(Profit)