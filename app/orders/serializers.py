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

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        if 'customer' in validated_data:
            customer_data = validated_data.pop("customer")
            instance.customer.customer_id = customer_data.get("customer_id", instance.customer.customer_id)
            instance.customer.delivery_type = customer_data.get("delivery_type", instance.customer.delivery_type)
            instance.customer.street = customer_data.get("street", instance.customer.street)
            instance.customer.city = customer_data.get("city", instance.customer.city)
            instance.customer.postal_code = customer_data.get("postal_code", instance.customer.postal_code)
            instance.customer.delivery_deadline = customer_data.get("delivery_deadline",
                                                                    instance.customer.delivery_deadline)
            instance.customer.self_pickup_hours = customer_data.get("self_pickup_hours",
                                                                    instance.customer.self_pickup_hours)
            instance.customer.save()

        if 'product' in validated_data:
            product_data = validated_data.pop("product")
            instance.product.product_id = product_data.get("product_id", instance.product.product_id)
            instance.product.height = product_data.get("height", instance.product.height)
            instance.product.width = product_data.get("width", instance.product.width)
            instance.product.length = product_data.get("length", instance.product.length)
            instance.product.materials = product_data.get("materials", instance.product.materials)
            instance.product.deadlines = product_data.get("deadlines", instance.product.deadlines)
            instance.product.delivery_terms = product_data.get("delivery_terms", instance.product.delivery_terms)
            instance.product.save()

        if 'price_product' in validated_data:
            price_product_data = validated_data.pop("price_product")
            instance.price_product.price = price_product_data.get("price", instance.price_product.price)
            instance.price_product.currency = price_product_data.get("currency", instance.price_product.currency)
            instance.price_product.production_cost = price_product_data.get("production_cost",
                                                                            instance.price_product.production_cost)
            instance.price_product.cost_delivery = price_product_data.get("cost_delivery",
                                                                          instance.price_product.cost_delivery)
            instance.price_product.order = price_product_data.get("order", instance.price_product.order)
            instance.price_product.margin = price_product_data.get("margin", instance.price_product.margin)
            instance.price_product.save()

        if 'executor' in validated_data:
            executor_data = validated_data.pop("executor")
            instance.executor.executor_id = executor_data.get("executor_id", instance.executor.executor_id)
            instance.executor.data_order_take = executor_data.get("data_order_take", instance.executor.data_order_take)
            instance.executor.order_execution_date = executor_data.get("order_execution_date",
                                                                       instance.executor.order_execution_date)
            instance.executor.actual_execution_date = executor_data.get("actual_execution_date",
                                                                        instance.executor.actual_execution_date)
            instance.executor.save()

        if 'delivery' in validated_data:
            delivery_data = validated_data.pop("delivery")
            instance.delivery.where_delivery = delivery_data.get("where_delivery", instance.delivery.where_delivery)
            instance.delivery.delivery_type = delivery_data.get("delivery_type", instance.delivery.delivery_type)
            instance.delivery.save()

        if "status_order" in validated_data:
            instance.status_order = validated_data.pop("status_order")

        instance.save()
        return instance
