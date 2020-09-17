from django.contrib import admin
from rest_framework import fields

from .models import Comment, Post


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('user', 'created')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post"""
    list_display = ('user', 'posted', 'description_brief')
    readonly_fields = ('user', 'posted')
    fields = ('user', 'posted', 'image', 'description')

    inlines = [CommentInline]
