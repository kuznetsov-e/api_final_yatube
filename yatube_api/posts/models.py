from django.contrib.auth import get_user_model
from django.db import models

from .constants import (GROUP_TITLE_MAX_LENGTH, POST_TEXT_TRUNCATION_LENGTH,
                        POST_UPLOAD_TO)

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=GROUP_TITLE_MAX_LENGTH,
        verbose_name='Название группы'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL группы'
    )
    description = models.TextField(
        verbose_name='Описание группы'
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста'
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        upload_to=POST_UPLOAD_TO, null=True, blank=True,
        verbose_name='Картинка'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:POST_TEXT_TRUNCATION_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField(
        verbose_name='Текст комментария'
    )
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created']

    def __str__(self):
        return self.text[:POST_TEXT_TRUNCATION_LENGTH]


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'following')

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
