# Generated by Django 4.2.11 on 2024-08-25 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0004_alter_orderfreelancemodel_order_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderfreelancemodel',
            name='order_type',
            field=models.IntegerField(choices=[(1, 'Заказ на модель'), (2, 'Заказ на модель с печатью')], verbose_name='Тип заказа'),
        ),
    ]
