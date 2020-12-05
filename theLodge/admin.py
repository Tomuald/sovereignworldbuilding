from django.contrib import admin

from theLodge.models import SharedItemlist

@admin.register(SharedItemlist)
class SharedItemlistAdmin(admin.ModelAdmin):
    pass
