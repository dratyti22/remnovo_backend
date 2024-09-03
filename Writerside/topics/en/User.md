#User

user information

user has fields in the database:

    password
    last_login
    is_superuser
    username
    first_name
    last_name
    email
    is_staff
    is_active
    data_joined
    id
    users_status
    token
    roles_id
    points
    successful_orders
    total_orders_placed

### Create User

need to:

    email
    password

api:

    /user/create?email=...&password=...

If registration (but not logged into your account) is successful, the following will be returned:

```Python
{'message': 'User created successfully'}, HTTP_201_CREATED
```

otherwise:

```Python
{'error': 'Failed to create user'}, HTTP_400_BAD_REQUEST
```

### Login User

need to:

    email
    password

api:

    /user/login?email=...&password=...

If successful, the user is logged in and returned:

```Python
{'message': 'User logged in successfully'}, HTTP_200_OK
```

if not then:

```Python
{'error': 'Failed to login user'}, HTTP_500_INTERNAL_SERVER_ERROR
```

### Auth Token

need to

    auth_token

api:

    /user/auth?auth_token=...

If successful, the user is logged in and returned:

```Python
{"message": "Login successfully"}, HTTP_200_OK
```

if not then:

```Python
{'error': 'Auth token verified successfully'}, HTTP_401_UNAUTHORIZED
```

### Email Login User

need to

    code

api:

    /user/email-confirmation?code=...

If successful, the user is logged in,
is_active changes to true and returns:

```Python
{'message': 'Email confirmed successfully'}, HTTP_200_OK
```

if not then:

```Python
{'error': 'Failed to confirm email'}, HTTP_400_BAD_REQUEST
```