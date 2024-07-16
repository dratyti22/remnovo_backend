from django.db import models


class Customer(models.Model):
    DELIVERY_TYPE = [
        (1, "Самовывоз"),
        (2, "Доставка на адрес"),
    ]
    customer_id = models.IntegerField(verbose_name="ID заказчика")
    delivery_type = models.IntegerField(choices=DELIVERY_TYPE, verbose_name="Тип доставки")

    street = models.CharField(max_length=255, verbose_name="Улица")
    city = models.CharField(max_length=100, verbose_name="Город")
    postal_code = models.CharField(max_length=10, verbose_name="Индекс")

    delivery_deadline = models.TextField(verbose_name="Сроки доставки")
    self_pickup_hours = models.TextField(null=True, blank=True, verbose_name="Когда работает")

    class Meta:
        db_table = "order_customer"
        verbose_name = 'Заказчик'
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return f"{self.customer_id} - {self.delivery_type}"


class Product(models.Model):
    product_id = models.IntegerField(verbose_name="Продукт id")
    height = models.FloatField(verbose_name='Высота')
    width = models.FloatField(verbose_name='Ширина')
    length = models.FloatField(verbose_name='Длина')
    materials = models.TextField(verbose_name="Материал")
    deadlines = models.TextField(verbose_name="Сроки выполнения")
    delivery_terms = models.TextField(verbose_name="Сроки доставки")

    class Meta:
        db_table = "order_product"
        verbose_name='Продукт'
        verbose_name_plural="Продукты"

    def __str__(self):
        return f"{self.product_id}"
