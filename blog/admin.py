from django.contrib import admin

from blog.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "author", "created_at", "updated_at")
    list_filter = ['created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "get_post_title", "created_at", "updated_at")

    def get_post_title(self, obj):
        return obj.post.title

    get_post_title.short_description = "Пост"
