from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile


class ProfileInline(admin.StackedInline):
    '''Admin View for Profile'''
    model = Profile
    filter_horizontal = ('followed', )


UserAdmin.inlines = [ProfileInline]
