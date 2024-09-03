# Freelance

information about Freelance

    crud-everything

## Path:

    /api/freelance/

### Example of the data that is coming in:

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

### Data to be deleted:

    {
        "order": 3,
        "order_type": 1,
        "total_amount": 3000,
        "our_model": false,
        "customer": 1
    }

#### Description of the field

order: id of the order to be made \
total_amount: Price. \
our_model: Our model. Literally false. \
customer: User id. \
order_type: What causes the indicator:

        (1, 'Model Order'),
        (2, 'Order for a model with an oven')

#### Search

    /api/freelance/?search=

Fields:

    order 
    order_type