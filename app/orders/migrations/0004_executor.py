# Generated by Django 4.2.11 on 2024-07-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_priceproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executor_id', models.IntegerField(verbose_name='Исполнитель id')),
                ('data_order_take', models.CharField(max_length=255, verbose_name='Дата взятия заказа')),
                ('order_execution_date', models.CharField(max_length=255, verbose_name='Дата исполнения по заказу')),
                ('actual_execution_date', models.CharField(max_length=255, verbose_name='Дата исполнения фактическая')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
                'db_table': 'order_executor',
            },
        ),
    ]
