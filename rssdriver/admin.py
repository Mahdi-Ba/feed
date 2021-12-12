from django.contrib import admin

from .models import Channel, Article


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    filter_horizontal = ('users',)
    list_display = ['title', 'status', 'is_disable', 'publish_date', 'last_build_date', 'language', ]
    list_filter = ['status', 'is_disable']
    search_fields = ['title']


@admin.register(Article)
class ChannelAdmin(admin.ModelAdmin):
    filter_horizontal = ('users',)
    list_display = ['title', 'publish_date']
    search_fields = ['title', 'author']
    list_filter = ['publish_date', ]



