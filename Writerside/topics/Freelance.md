# Freelance

информация о Freelance

    crud - все

## Путь:

    /api/freelance/

### Пример данных которые приходят:

    {
        "id": 1,
        "order": 1,
        "order_type": 1,
        "total_amount": "100.00",
        "our_model": true,
        "created_at": "2024-07-31T16:24:17.689738+03:00",
        "updated_at": "2024-07-31T16:24:17.689765+03:00",
        "customer": 1
    }

### Данные которые надо отсылать:

    {
        "order": 3,
        "order_type": 1,
        "total_amount": 3000,
        "our_model": false,
        "customer": 1
    }

#### Описание полей

order: id заказа которого надо делать \
total_amount: Цена. \
our_model: Нашали модель. Изначально false. \
customer: id Пользователя. \
order_type: Что означает индикатор:

        (1, 'Заказ на модель'),
        (2, 'Заказ на модель с печатью')

#### Поиск

    /api/freelance/?search=

Поля:

    order 
    order_type 
