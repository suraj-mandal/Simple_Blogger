from django.contrib import admin

from blog.models import Post


# Register your models here.


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'date_posted']

    fieldsets = (
        ('DETAILS', {
            'fields': ['title', 'content', 'author']
        }), (
            'CREATION DATE', {
                'fields': ['date_posted']
            }
        )
    )
