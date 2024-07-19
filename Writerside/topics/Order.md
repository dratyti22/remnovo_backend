# Order

информация о Order

## Путь:

    /api/order

### Пример данных которые приходят:

    {
        "id": 1,
        "customer": {
            "id": 1,
            "customer_id": 1,
            "delivery_type": 1,
            "street": "2",
            "city": "2",
            "postal_code": "32",
            "delivery_deadline": "fafa",
            "self_pickup_hours": "afsaf"
        },
        "product": {
            "id": 1,
            "product_id": 1,
            "height": 2.0,
            "width": 2.0,
            "length": 2.0,
            "materials": "asfa",
            "deadlines": "fsfa",
            "delivery_terms": "fasfas"
        },
        "price_product": {
            "id": 1,
            "price": 1223.0,
            "currency": "rub",
            "production_cost": 324.42,
            "cost_delivery": 32.111,
            "order": false,
            "margin": 1000.0
        },
        "executor": {
            "id": 1,
            "executor_id": 2,
            "data_order_take": "12fafd",
            "order_execution_date": "fasd",
            "actual_execution_date": "fasfas"
        },
        "delivery": {
            "id": 1,
            "where_delivery": "fafdasfas",
            "delivery_type": "2"
        },
        "status_order": "4"
    },

### Данные которые надо отсылать:

    {
        "id": делается овтоматически,
        "customer": {
            "id": делается овтоматически,
            "customer_id": intejetr,
            "delivery_type": intejer,
            "street": "string",
            "city": "string",
            "postal_code": "string",
            "delivery_deadline": "string",
            "self_pickup_hours": "string"
        },
        "product": {
            "id": делается овтоматически,
            "product_id": integer,
            "height": float or integer,
            "width": float or integer,
            "length": float or integer,
            "materials": "string",
            "deadlines": "string",
            "delivery_terms": "string"
        },
        "price_product": {
            "id": делается овтоматически,
            "price": float or integer,
            "currency": "string",
            "production_cost": float or integer,
            "cost_delivery": float or integer,
            "order": True or False,
            "margin": float or integer
        },
        "executor": {
            "id": делается овтоматически,
            "executor_id": integer,
            "data_order_take": "string",
            "order_execution_date": "string",
            "actual_execution_date": "string"
        },
        "delivery": {
            "id": делается овтоматически,
            "where_delivery": "string",
            "delivery_type": integer
        },
        "status_order": integer"
    }
