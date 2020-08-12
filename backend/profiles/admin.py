from django.contrib import admin

from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = (
        'user',
        'bio',
    )
    # list_filter = ('',)
    # inlines = [
    #     'PostInline',
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('', )
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
