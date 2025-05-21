from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from blog.constants import LEN_NAME, LEN_MODEL_TEXT
from core.models import PublicationModel

User = get_user_model()


class Location(PublicationModel):
    name = models.CharField(max_length=LEN_NAME, verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:LEN_MODEL_TEXT]


class Category(PublicationModel):
    title = models.CharField(max_length=LEN_NAME, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.'
                   )
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:LEN_MODEL_TEXT]


class Post(PublicationModel):
    title = models.CharField(max_length=LEN_NAME, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=('Если установить дату и время в будущем — можно делать '
                   'отложенные публикации.'
                   )
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    location = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        verbose_name='Местоположение',
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    image = models.ImageField('Фото', upload_to='posts_images', blank=True)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title[:LEN_MODEL_TEXT]

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (
            f'Комментрарий - {self.text[:LEN_MODEL_TEXT]}, '
            f'Пост - {self.post}, '
            f'Автор - {self.author}'
        )
