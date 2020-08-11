from django.contrib import admin

from .models import Comment, Post


class CommentInline(admin.StackedInline):
    model = Comment
    ordering = ('created', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post"""
    list_display = ('user', 'posted', 'description_brief')
    readonly_fields = ('posted', )

    inlines = [CommentInline]
