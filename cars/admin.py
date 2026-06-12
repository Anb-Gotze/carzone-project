from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    @admin.display(description='Car Image')
    def thumbnail(self, obj):
        if obj.car_photo:
            return format_html(
                '<img src="{}" width="40" style="border-radius:50%;" />',
                obj.car_photo.url
            )
        return "No Image"
    list_display = ('id', 'thumbnail', 'car_title','city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured',)
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type',)
    list_filter = ('city', 'model', 'body_style', 'fuel_type',)
admin.site.register(Car, CarAdmin)