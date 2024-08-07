# Generated by Django 4.2.11 on 2024-07-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_type',
            field=models.CharField(choices=[('1', 'Самовывоз'), ('2', 'Курьер'), ('3', 'Постамат')], max_length=255, verbose_name='Тип доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status_order',
            field=models.CharField(choices=[('1', 'Отложенный'), ('2', 'Ждет выбора исполнителя'), ('3', 'В печати'), ('4', 'Готов'), ('5', 'Просрочен в печати'), ('6', 'Выполнен'), ('7', 'Отменен')], max_length=255, verbose_name='Статус'),
        ),
    ]
