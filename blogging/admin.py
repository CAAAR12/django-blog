from django.contrib import admin
from blogging.models import Post,Category


class CategoryInLine(admin.StackedInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'text',
                    'author',
                    'created_date','modified_date','published_date')
    inlines = [CategoryInLine]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)