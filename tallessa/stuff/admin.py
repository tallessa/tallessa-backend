from django.contrib import admin

from .models import Item, Location


class ItemAdmin(admin.ModelAdmin):
    list_display = ('team', 'slug', 'name')
    list_filter = ('team',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('team', 'slug', 'name')
    list_filter = ('team',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Location, LocationAdmin)
