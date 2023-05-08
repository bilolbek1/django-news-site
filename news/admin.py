from django.contrib import admin
from .models import News, Category, Contact, Comment
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'status', 'image']
    list_filter = ['status', 'publish_time', 'created_time', 'image']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'status']
    ordering = ['status', 'publish_time']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'body', 'created_time', 'active']
    list_filter = ['body', 'created_time']
    search_fields = ['user', 'body']

    def disable_comment(self, request, queryset):
        return queryset.update(active=False)

    def enable_comment(self, request, queryset):
        return queryset.update(active=True)
