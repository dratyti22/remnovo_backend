from datetime import datetime

from django.db import models
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey


class Tags(MPTTModel):
    time_create = models.BigIntegerField(
        verbose_name='Время добавления', blank=True
    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель')
    section = models.BooleanField(default=False, verbose_name='Раздел')
    name = models.CharField(max_length=150, unique=True, verbose_name='Название категории')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'tag'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.time_create:
            self.time_create = int(datetime.now().timestamp())
        super().save(*args, **kwargs)


class Material(models.Model):
    name = models.CharField(max_length=500, unique=True, verbose_name="Название")
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'material'
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'


class File(models.Model):
    time_create = models.BigIntegerField(
        verbose_name='Время добавления', blank=True
    )
    filename = models.CharField(max_length=500, unique=True, verbose_name="Имя файла")
    owners = models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Владельцы')
    height = models.FloatField(verbose_name='Высота')
    width = models.FloatField(verbose_name='Ширина')
    length = models.FloatField(verbose_name='Длина')
    materials = models.ManyToManyField('Material')
    STATUS_CHOICES = [
        (0, 'не проверено'),
        (1, 'активно'),
        (2, 'забанено'),
        (3, 'нельзя удалять или отключать'),
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        db_table = 'file'
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ["-filename"]
        indexes = [
            models.Index(fields=['filename'], name='filename_idx'),
            models.Index(fields=['status'], name='status_idx'),
        ]

    def __str__(self):
        return self.filename

    def save(self, *args, **kwargs):
        if not self.time_create:
            self.time_create = int(datetime.now().timestamp())
        super().save(*args, **kwargs)


class DescriptionFile(models.Model):
    time_create = models.BigIntegerField(
        verbose_name='Время добавления', blank=True
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='description_file', verbose_name='File')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    title = models.CharField(max_length=300, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    line_video = models.URLField(verbose_name='Ссылка на видео')
    tags = models.ManyToManyField(Tags, blank=True, verbose_name='Теги')

    class Meta:
        db_table = 'description_file'
        verbose_name = 'Описание файла'
        verbose_name_plural = 'Описание файла'
        ordering = ['-title', '-file']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['description']),
        ]

    def __str__(self):
        return f"{self.file.filename}-{self.title}"

    def save(self, *args, **kwargs):
        if not self.time_create:
            self.time_create = int(datetime.now().timestamp())
        super().save(*args, **kwargs)


class ImageFile(models.Model):
    description_file = models.ForeignKey(to=DescriptionFile, on_delete=models.CASCADE, related_name='image_file',
                                         verbose_name='File')

    image = models.ImageField(upload_to='file_image', verbose_name='Изображение', null=True, blank=True)

    class Meta:
        db_table = 'image_file'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
