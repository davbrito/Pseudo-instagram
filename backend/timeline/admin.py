from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post"""
    list_display = ('user', 'posted', 'description_brief')
    readonly_fields = ('posted', )
