# Generated by Django 4.2.11 on 2024-07-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_executor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('where_delivery', models.CharField(max_length=255, verbose_name='Где заказчик получит свой товар')),
                ('delivery_type', models.CharField(choices=[(1, 'Самовывоз'), (2, 'Курьер'), (3, 'Постамат')], max_length=255, verbose_name='Тип доставки')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
                'db_table': 'order_delivery',
            },
        ),
    ]