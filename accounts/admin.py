# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = CustomUser
	list_display = ['username', 'email']
	
	fieldsets = UserAdmin.fieldsets + (
		('User Library', {'fields': ('user_library', )}),
	)
	
	filter_horizontal = ('user_library', 'groups', 'user_permissions', )

admin.site.register(CustomUser, CustomUserAdmin)

