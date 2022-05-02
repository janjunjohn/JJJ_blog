from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Blog, Tag


class BlogAdmin(MarkdownxModelAdmin):
    list_display = (
        'title',
        'get_tags',
        'is_public',
        'pub_date',
    )
    list_display_links = list_display
    
    def get_tags(self, row):
        return ''.join([tag.name for tag in row.tags.all()])

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)

