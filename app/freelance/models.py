from django.db import models
from app.users.models import CustomUser
from app.orders.models import Order


class OrderFreelanceModel(models.Model):
    order = models.PositiveIntegerField(verbose_name="Номер заказа")
    order_type_choices = (
        ('model', 'Заказ на модель'),
        ('model_print', 'Заказ на модель с печатью')
    )
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='customer_orders',
                                 verbose_name="Покупатель")
    order_type = models.CharField(max_length=20, choices=order_type_choices, verbose_name="Тип заказа")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    our_model = models.BooleanField(default=True, verbose_name="Наша модель")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        db_table = "freelance_order"
        verbose_name = "Фриланс"
        verbose_name_plural = "Фриланс"

    def __str__(self):
        return f"{self.order}-{self.our_model}"
