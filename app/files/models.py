from django.db import models
from django.contrib.auth.models import User


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
    filename = models.CharField(max_length=500, unique=True, verbose_name="Имя файла")
    owners = models.ManyToManyField(to=User, verbose_name='Владельцы')
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
