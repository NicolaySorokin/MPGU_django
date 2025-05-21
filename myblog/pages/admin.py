from django.contrib import admin

from .models import StaticPage


@admin.register(StaticPage)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'context'
    )
