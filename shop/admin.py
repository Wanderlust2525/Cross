from typing import Type
from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Category, Brand, Shops, Size, Type


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Type)


@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'articul','type','brand','category','price','date', 'sale','get_image')
    list_display_links = ('id', 'name', 'articul')
    search_fields = [
        'name',
        'articul',
        'description',
        'season',
        'category__name',
        'type__name',
    ]
    list_filter = ('category','type','price','date','brand','sale')
    list_editable = ('sale',)
    readonly_fields = ('views', 'date','last_update','get_full_image' )



    @admin.display(description='Изображение')
    def get_image(self, shop):
            if shop.image:  # Проверяем, есть ли файл изображения
                return mark_safe(f'<img src="{shop.image.url}" width="100px">')
            return "Нет изображения"
        
    @admin.display(description='Изображение')
    def get_full_image(self,shop):
            return mark_safe(f'<img src ="{shop.image.url}" width="75%">')

# Register your models here.
