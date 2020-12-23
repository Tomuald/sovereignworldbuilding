from django.contrib import admin

from theLodge.models import SharedItemlist, SharedUniverse

@admin.register(SharedItemlist)
class SharedItemlistAdmin(admin.ModelAdmin):
    pass

@admin.register(SharedUniverse)
class SharedUniverseAdmin(admin.ModelAdmin):
    pass
