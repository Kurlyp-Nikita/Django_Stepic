from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):  # Пользовательский менеджер модели
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)  # Виджеты для заполнения полей


class Women(models.Model):
    class Status(models.IntegerChoices):  # Создание перечисления
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)  # Виджеты для заполнения полей

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
