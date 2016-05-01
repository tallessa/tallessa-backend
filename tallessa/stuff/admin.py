from django.contrib import admin

from .models import Item, Location


class ItemAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'slug', 'name')
    list_filter = ('tenant',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'slug', 'name')
    list_filter = ('tenant',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
