from .models import Customer, Product, PriceProduct, Executor, Delivery, Order

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PriceProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceProduct
        fields = '__all__'


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    product = ProductSerializer()
    price_product = PriceProductSerializer()
    executor = ExecutorSerializer()
    delivery = DeliverySerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        product_data = validated_data.pop('product')
        price_product_data = validated_data.pop('price_product')
        executor_data = validated_data.pop('executor')
        delivery_data = validated_data.pop('delivery')

        customer = Customer.objects.create(**customer_data)
        product = Product.objects.create(**product_data)
        price_product = PriceProduct.objects.create(**price_product_data)
        executor = Executor.objects.create(**executor_data)
        delivery = Delivery.objects.create(**delivery_data)

        order = Order.objects.create(
            customer=customer,
            product=product,
            price_product=price_product,
            executor=executor,
            delivery=delivery,
            **validated_data
        )

        return order
