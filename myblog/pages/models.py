from django.db import models


class StaticPage(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    context = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статичная страница'
        verbose_name_plural = 'статичные страницы'
