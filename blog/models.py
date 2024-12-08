from django.db import models

from user.models import NULLABLE

from config.settings import AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )

    text = models.TextField(
        verbose_name="Текст"
    )

    image = models.ImageField(
        upload_to='post_images/',
        **NULLABLE,
        verbose_name="Изображение"
    )

    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор"
    )

    comments = models.ManyToManyField(
        'Comment',
        related_name='post_comments',
        blank=True,
        verbose_name="Комментарии"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор"
    )

    text = models.TextField(
        verbose_name="Текст комментария"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"Комментарий от {self.author.username} на пост {self.post.title}"
