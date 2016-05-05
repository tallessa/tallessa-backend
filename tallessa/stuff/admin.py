from django.contrib import admin

from .models import Item, Place


class ItemAdmin(admin.ModelAdmin):
    list_display = ('team', 'slug', 'name')
    list_filter = ('team',)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('team', 'slug', 'name')
    list_filter = ('team',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Place, PlaceAdmin)
