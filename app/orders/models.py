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
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.product_id}"


class PriceProduct(models.Model):
    price = models.FloatField(verbose_name='Цена')
    currency = models.CharField(max_length=100, verbose_name="Валюта")
    production_cost = models.FloatField(verbose_name="Стоимость изготовления")
    cost_delivery = models.FloatField(verbose_name="Стоимость доставки")
    order = models.BooleanField(default=False, verbose_name="Заказ заказан или нет")
    margin = models.FloatField(verbose_name="Маржа")

    class Meta:
        db_table = "order_price_product"
        verbose_name = "Цена товара"
        verbose_name_plural = "Цена товаров"

    def __str__(self):
        return f"{self.price} - {self.currency}"


class Executor(models.Model):
    executor_id = models.IntegerField(verbose_name="Исполнитель id")
    data_order_take = models.CharField(max_length=255, verbose_name="Дата взятия заказа")
    order_execution_date = models.CharField(max_length=255, verbose_name="Дата исполнения по заказу")
    actual_execution_date = models.CharField(max_length=255, verbose_name="Дата исполнения фактическая")

    class Meta:
        db_table = "order_executor"
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self):
        return f"{self.executor_id}"


class Delivery(models.Model):
    where_delivery = models.CharField(max_length=255, verbose_name="Где заказчик получит свой товар")
    DELIVERY_TYPE = [
        ('1', "Самовывоз"),
        ('2', "Курьер"),
        ('3', "Постамат"),
    ]
    delivery_type = models.CharField(max_length=255, verbose_name="Тип доставки", choices=DELIVERY_TYPE)

    class Meta:
        db_table = 'order_delivery'
        verbose_name = "Доставка"
        verbose_name_plural = "Доставки"

    def __str__(self):
        return f"{self.where_delivery} - {self.delivery_type}"


class Order(models.Model):
    STATUS_ORDERS = [
        ('1', "Отложенный"),
        ('2', "Ждет выбора исполнителя"),
        ('3', "В печати"),
        ('4', "Готов"),
        ('5', "Просрочен в печати"),
        ('6', "Выполнен"),
        ('7', "Отменен"),
    ]
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    price_product = models.ForeignKey(to=PriceProduct, on_delete=models.CASCADE, related_name='orders')
    executor = models.ForeignKey(to=Executor, on_delete=models.CASCADE)
    delivery = models.ForeignKey(to=Delivery, on_delete=models.CASCADE)
    status_order = models.CharField(max_length=255, verbose_name="Статус", choices=STATUS_ORDERS)

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return str(self.status_order)
