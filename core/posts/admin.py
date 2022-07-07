from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'owner', 'created_at', 'likes']
    fields = ['content', 'owner']
    search_fields = ['content', 'owner']
    list_filter = ['owner']
    readonly_fields = ['id']
