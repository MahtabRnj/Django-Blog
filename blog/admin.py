from django.contrib import admin
from .models import Article, Category


@admin.action(description='انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')

    if rows_updated == 1:
        message_bit = 'منتشر شد'
    else:
        message_bit = 'منتشر شدند'
    modeladmin.message_user(request, f"{rows_updated} مقاله {message_bit} ")


@admin.action(description='پیش نویس مقالات انتخاب شده')
def make_draft(modeladmin, request, queryset):
    rows_updated = queryset.update(status='d')
    if rows_updated == 1:
        message_bit = ' پیش نویس شد'
    else:
        message_bit = 'پیش نویس شدند'
    modeladmin.message_user(request, f"{rows_updated} مقاله {message_bit}")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['parent__id']


admin.site.register(Category, CategoryAdmin)


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag', 'status', 'jpublish', 'category_to_str')
    list_filter = ('status', 'publish')
    search_fields = ('description', 'title')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'publish')
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published()])

    category_to_str.short_description = 'دسته بندی'


admin.site.register(Article, ArticleAdmin)
