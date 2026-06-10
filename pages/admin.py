from django.contrib import admin
from .models import Team
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):

    @admin.display(description='Photo')
    def thumbnail(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="40" style="border-radius:50%;" />',
                obj.photo.url
            )
        return "No Image"

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, TeamAdmin)